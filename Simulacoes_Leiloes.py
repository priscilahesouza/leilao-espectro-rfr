import numpy as np
import matplotlib.pyplot as plt

np.random.seed(23)


# Parameters
n_E = 3  # number of entrants
n_I = 3  # number of incumbents
n_sim = 10000  # number of simulations
theta = 0.7  # upper bound for entrants in asymmetric scenario

# Helper functions
def simulate_spa(values):
    winner = np.argmax(values)
    sorted_values = np.sort(values)
    payment = sorted_values[-2]
    efficiency = 1  # always efficient
    return payment, efficiency, None

def simulate_fpa(values):
    bids = (len(values) - 1) / len(values) * values
    winner = np.argmax(bids)
    payment = bids[winner]
    efficiency = 1  # always efficient
    return payment, efficiency, None

def simulate_mechanism_a(v_E, v_I):
    bids_E = (n_E - 1) / n_E * v_E
    winner_E = np.argmax(bids_E)
    if np.all(bids_E == 0):
        bids_I = (n_I - 1) / n_I * v_I
        winner_I = np.argmax(bids_I)
        payment = bids_I[winner_I]
        winner_value = v_I[winner_I]
    else:
        payment = bids_E[winner_E]
        winner_value = v_E[winner_E]
    all_values = np.concatenate([v_E, v_I])
    efficiency = 1 if winner_value == np.max(all_values) else 0
    return payment, efficiency, None

def simulate_mechanism_b(v_E, v_I):
    # Agora incumbentes ofertam seus valores verdadeiros (não o lance de equilíbrio FPA)
    bids_I = v_I  
    max_bid_I = np.max(bids_I)
    max_val_E = np.max(v_E)
    if max_val_E >= max_bid_I:
        payment = max_bid_I
        winner_value = max_val_E
        entry = 1
    else:
        payment = max_bid_I
        winner_value = v_I[np.argmax(bids_I)]
        entry = 0
    all_values = np.concatenate([v_E, v_I])
    efficiency = 1 # always efficient
    return payment, efficiency, entry

# Simulation function
def run_simulation(asymmetric=False):
    results = {'SPA': [], 'FPA': [], 'A': [], 'B': []}
    for _ in range(n_sim):
        if asymmetric:
            v_E = np.random.uniform(0, theta, n_E)
        else:
            v_E = np.random.uniform(0, 1, n_E)
        v_I = np.random.uniform(0, 1, n_I)
        values = np.concatenate([v_E, v_I])

        results['SPA'].append(simulate_spa(values))
        results['FPA'].append(simulate_fpa(values))
        results['A'].append(simulate_mechanism_a(v_E, v_I))
        results['B'].append(simulate_mechanism_b(v_E, v_I))
    return results

# Run simulations
results_sym = run_simulation(asymmetric=False)
results_asym = run_simulation(asymmetric=True)

# Aggregation function
def aggregate_results(results):
    revenue = {k: np.mean([x[0] for x in v]) for k, v in results.items()}
    efficiency = {k: np.mean([x[1] for x in v]) for k, v in results.items()}
    entry = {k: np.mean([x[2] for x in v if x[2] is not None]) if any(x[2] is not None for x in v) else 0 for k, v in results.items()}
    return revenue, efficiency, entry

rev_sym, eff_sym, ent_sym = aggregate_results(results_sym)
rev_asym, eff_asym, ent_asym = aggregate_results(results_asym)

# Plotting
def plot_metric(metric_sym, metric_asym, title, ylabel, filename):
    labels = list(metric_sym.keys())
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar(x - width/2, [metric_sym[k] for k in labels], width, label='Simétrico')
    ax.bar(x + width/2, [metric_asym[k] for k in labels], width, label='Assimétrico')

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

plot_metric(rev_sym, rev_asym, 'Receita Esperada do Leiloeiro', 'Receita Média', 'grafico_receita.png')
plot_metric(eff_sym, eff_asym, 'Eficiência Alocativa', 'Probabilidade de Alocação Eficiente', 'grafico_eficiencia.png')
plot_metric(ent_sym, ent_asym, 'Frequência de Entrada (Mecanismo B)', 'Frequência Média', 'grafico_entrada.png')

print("Simulações concluídas e gráficos gerados.")

