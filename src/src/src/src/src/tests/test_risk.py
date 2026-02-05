from src.risk_calculator import water_scarcity_score

def test_score():
    score = water_scarcity_score(precip_mm=800, usage_liters_per_day=100, pop_density=50)
    assert 0 <= score <= 10
    print("Risk score test passed!")

if __name__ == "__main__":
    test_score()
