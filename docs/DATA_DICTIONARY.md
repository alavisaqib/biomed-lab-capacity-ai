# Data dictionary

All inputs and training records are synthetic. Fields are numeric; counts and cents must be integers.

- `queue_samples` — Samples in queue; valid range 0–1000; integer.
- `instruments` — Available instruments; valid range 1–12; integer.
- `minutes_per_sample` — Processing time (min); valid range 1–120; real number.
- `urgent_samples` — Urgent samples; valid range 0–1000; integer.

`target`: turnaround_hours in hours.

Queue-clearance time plus an urgent-workload adjustment and Gaussian noise generates synthetic turnaround labels. A random split tests interpolation, not temporal or site generalization.
