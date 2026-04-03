import pandas as pd
import xgboost as xgb
import time
import sys
sys.path.insert(0, '/home/vedant/Desktop/vs_code-project_folder/machine learning projects/fraud detection system')

from pipeline.feature_engineering import engineer_features

def benchmark_inference():
    """Benchmark inference latency to ensure <100ms p99"""

    # Load model
    model = xgb.XGBClassifier()
    model.load_model("models/fraud_xgb.json")

    # Sample transactions
    sample_features = pd.DataFrame({
        'mean_amount': [1500.0, 2000.0, 800.0],
        'total_amount': [15000.0, 8000.0, 4000.0],
        'transaction_count': [10, 4, 5]
    })

    # Warm up
    _ = model.predict(sample_features)

    # Benchmark - 100 predictions
    latencies = []
    for _ in range(100):
        start = time.perf_counter()
        _ = model.predict(sample_features.iloc[:1])
        latencies.append((time.perf_counter() - start) * 1000)  # Convert to ms

    latencies.sort()
    p50 = latencies[49]
    p99 = latencies[98]
    p999 = latencies[99]
    avg = sum(latencies) / len(latencies)

    print("Inference Latency Benchmarks (ms):")
    print(f"  Average: {avg:.2f}ms")
    print(f"  P50:     {p50:.2f}ms")
    print(f"  P99:     {p99:.2f}ms")
    print(f"  P999:    {p999:.2f}ms")

    if p99 < 100:
        print(f"✓ Latency test PASSED - P99 {p99:.2f}ms < 100ms")
        return True
    else:
        print(f"✗ Latency test FAILED - P99 {p99:.2f}ms >= 100ms")
        return False

if __name__ == "__main__":
    success = benchmark_inference()
    sys.exit(0 if success else 1)
