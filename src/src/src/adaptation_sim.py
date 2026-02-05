def simulate_adaptations(risk_score, leak_reduction=0.25, irrigation_efficiency=0.40):
    """
    Estimate risk reduction from interventions.
    - Leak detection: reduce non-revenue water 25%.
    - Smart irrigation: save 40% in ag use.
    """
    reductions = {
        'Leak Detection': risk_score * leak_reduction,
        'Smart Irrigation': risk_score * irrigation_efficiency,
        'Combined': risk_score * (leak_reduction + irrigation_efficiency - 0.1)  # some overlap
    }
    return reductions

# Example
if __name__ == "__main__":
    risk = 7.5
    print(simulate_adaptations(risk))
