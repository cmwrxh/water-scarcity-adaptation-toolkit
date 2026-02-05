import numpy as np

def water_scarcity_score(precip_mm=500, usage_liters_per_day=200, pop_density=100, drought_factor=1.2):
    """
    Simple score (0-10): higher = more scarcity risk.
    - Low precip + high usage + density + climate stress.
    """
    base = 10 - (precip_mm / 100)  # inverse precip
    usage_penalty = usage_liters_per_day / 100
    density_penalty = pop_density / 50
    score = (base + usage_penalty + density_penalty) * drought_factor
    return np.clip(score, 0, 10)

# Example
if __name__ == "__main__":
    print(f"Risk score: {water_scarcity_score():.1f}/10")
