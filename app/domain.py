import math
from .models import predict
from .config import SPEC

def transform(features):
    return [features[name] for name in SPEC['model_features']]

def result(action, summary, signals, steps):
    return {'minimum_action':action, 'summary':summary, 'signals':signals, 'next_steps':steps}

def analyze(f):
    if f['urgent_samples'] > f['queue_samples']:
        raise ValueError('Urgent samples cannot exceed the total queue')
    predicted, residual = predict(f)
    clearance=f['queue_samples']*f['minutes_per_sample']/f['instruments']/60
    action='escalate' if clearance>24 else 'review' if clearance>8 else 'monitor'
    return result(action, f'Estimated turnaround {max(0,predicted):.1f} h; theoretical queue clearance {clearance:.1f} h.',
        {'predicted_turnaround_h':round(max(0,predicted),2),'queue_clearance_h':round(clearance,2),'heldout_residual_p90_h':round(residual,2)},
        ['Confirm instrument availability and staffing coverage.', 'Ask the laboratory supervisor to review capacity before changing sample routing.'])

def simulate(rng):
    queue=int(rng.integers(5,400)); instruments=int(rng.integers(1,9)); minutes=rng.uniform(5,40); urgent=int(rng.integers(0,queue+1))
    target=max(0,queue*minutes/instruments/60+urgent*.025+rng.normal(0,1.2))
    return [queue,instruments,minutes,urgent], target
