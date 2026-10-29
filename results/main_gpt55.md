counts: {'C_naive': 20, 'C_msg': 20, 'C_full': 20, 'H_comp': 20, 'H_high': 20, 'C_adapt': 20, 'C_price': 20}

| negatives | positives | detector | AUROC [95% CI] | TPR@FPR<=10% (FPR) |
|---|---|---|---|---|
| neg=all honest | C_naive | M | 0.996 [0.98, 1.00] | 1.00 (0.07) |
| neg=all honest | C_naive | A | 0.537 [0.37, 0.69] | 0.20 (0.10) |
| neg=all honest | C_naive | idx_last3 | 0.994 [0.97, 1.00] | 1.00 (0.10) |
| neg=all honest | C_naive | hold_rate | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=all honest | C_naive | C | 1.000 [1.00, 1.00] | 1.00 (0.05) |
| neg=all honest | C_naive | S | 1.000 [1.00, 1.00] | 1.00 (0.05) |
| neg=all honest | C_naive | OW | 1.000 [1.00, 1.00] | 1.00 (0.05) |
| neg=all honest | C_naive | OWcal | 0.975 [0.94, 1.00] | 1.00 (0.10) |
| neg=all honest | C_naive | OWcal_hold | 0.975 [0.94, 1.00] | 1.00 (0.10) |
| neg=all honest | C_msg | M | 0.206 [0.10, 0.32] | 0.00 (0.07) |
| neg=all honest | C_msg | A | 0.422 [0.27, 0.57] | 0.00 (0.10) |
| neg=all honest | C_msg | idx_last3 | 0.966 [0.91, 1.00] | 0.95 (0.10) |
| neg=all honest | C_msg | hold_rate | 0.991 [0.97, 1.00] | 0.95 (0.10) |
| neg=all honest | C_msg | C | 0.175 [0.08, 0.29] | 0.00 (0.05) |
| neg=all honest | C_msg | S | 0.189 [0.09, 0.30] | 0.00 (0.05) |
| neg=all honest | C_msg | OW | 0.136 [0.06, 0.24] | 0.00 (0.05) |
| neg=all honest | C_msg | OWcal | 0.246 [0.13, 0.38] | 0.00 (0.10) |
| neg=all honest | C_msg | OWcal_hold | 0.964 [0.91, 1.00] | 0.95 (0.10) |
| neg=all honest | C_full | M | 0.239 [0.13, 0.36] | 0.00 (0.07) |
| neg=all honest | C_full | A | 0.214 [0.11, 0.33] | 0.00 (0.10) |
| neg=all honest | C_full | idx_last3 | 0.996 [0.98, 1.00] | 1.00 (0.10) |
| neg=all honest | C_full | hold_rate | 0.968 [0.92, 1.00] | 0.95 (0.10) |
| neg=all honest | C_full | C | 0.118 [0.04, 0.21] | 0.00 (0.05) |
| neg=all honest | C_full | S | 0.168 [0.07, 0.28] | 0.00 (0.05) |
| neg=all honest | C_full | OW | 0.055 [0.01, 0.12] | 0.00 (0.05) |
| neg=all honest | C_full | OWcal | 0.095 [0.04, 0.18] | 0.00 (0.10) |
| neg=all honest | C_full | OWcal_hold | 0.929 [0.85, 0.98] | 0.75 (0.10) |
| neg=all honest | C_adapt | M | 0.064 [0.02, 0.13] | 0.00 (0.07) |
| neg=all honest | C_adapt | A | 0.296 [0.16, 0.44] | 0.00 (0.10) |
| neg=all honest | C_adapt | idx_last3 | 0.916 [0.84, 0.98] | 0.80 (0.10) |
| neg=all honest | C_adapt | hold_rate | 0.704 [0.56, 0.84] | 0.10 (0.10) |
| neg=all honest | C_adapt | C | 0.103 [0.04, 0.19] | 0.00 (0.05) |
| neg=all honest | C_adapt | S | 0.077 [0.02, 0.15] | 0.00 (0.05) |
| neg=all honest | C_adapt | OW | 0.079 [0.03, 0.15] | 0.00 (0.05) |
| neg=all honest | C_adapt | OWcal | 0.160 [0.06, 0.27] | 0.00 (0.10) |
| neg=all honest | C_adapt | OWcal_hold | 0.627 [0.47, 0.78] | 0.00 (0.10) |
| neg=all honest | C_price | M | 0.069 [0.02, 0.14] | 0.00 (0.07) |
| neg=all honest | C_price | A | 0.284 [0.16, 0.43] | 0.00 (0.10) |
| neg=all honest | C_price | idx_last3 | 0.539 [0.39, 0.69] | 0.15 (0.10) |
| neg=all honest | C_price | hold_rate | 0.554 [0.39, 0.71] | 0.10 (0.10) |
| neg=all honest | C_price | C | 0.105 [0.04, 0.19] | 0.00 (0.05) |
| neg=all honest | C_price | S | 0.087 [0.03, 0.17] | 0.00 (0.05) |
| neg=all honest | C_price | OW | 0.069 [0.02, 0.14] | 0.00 (0.05) |
| neg=all honest | C_price | OWcal | 0.144 [0.06, 0.26] | 0.00 (0.10) |
| neg=all honest | C_price | OWcal_hold | 0.455 [0.30, 0.61] | 0.00 (0.10) |
| neg=all honest | pooled | M | 0.315 [0.23, 0.41] | 0.20 (0.07) |
| neg=all honest | pooled | A | 0.350 [0.26, 0.45] | 0.04 (0.10) |
| neg=all honest | pooled | idx_last3 | 0.882 [0.83, 0.93] | 0.78 (0.10) |
| neg=all honest | pooled | hold_rate | 0.844 [0.78, 0.90] | 0.62 (0.10) |
| neg=all honest | pooled | C | 0.300 [0.21, 0.39] | 0.20 (0.05) |
| neg=all honest | pooled | S | 0.304 [0.22, 0.40] | 0.20 (0.05) |
| neg=all honest | pooled | OW | 0.268 [0.19, 0.36] | 0.20 (0.05) |
| neg=all honest | pooled | OWcal | 0.324 [0.24, 0.41] | 0.20 (0.10) |
| neg=all honest | pooled | OWcal_hold | 0.790 [0.71, 0.87] | 0.54 (0.10) |
| neg=H_high | C_naive | M | 0.991 [0.97, 1.00] | 1.00 (0.05) |
| neg=H_high | C_naive | A | 0.464 [0.29, 0.64] | 0.10 (0.10) |
| neg=H_high | C_naive | idx_last3 | 0.988 [0.95, 1.00] | 1.00 (0.10) |
| neg=H_high | C_naive | hold_rate | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_high | C_naive | C | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_high | C_naive | S | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_high | C_naive | OW | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_high | C_naive | OWcal | 0.950 [0.88, 1.00] | 1.00 (0.10) |
| neg=H_high | C_naive | OWcal_hold | 0.950 [0.88, 1.00] | 1.00 (0.10) |
| neg=H_high | C_msg | M | 0.020 [0.00, 0.07] | 0.00 (0.05) |
| neg=H_high | C_msg | A | 0.335 [0.19, 0.52] | 0.00 (0.10) |
| neg=H_high | C_msg | idx_last3 | 0.943 [0.85, 1.00] | 0.90 (0.10) |
| neg=H_high | C_msg | hold_rate | 0.983 [0.94, 1.00] | 0.95 (0.10) |
| neg=H_high | C_msg | C | 0.033 [0.00, 0.12] | 0.00 (0.10) |
| neg=H_high | C_msg | S | 0.019 [0.00, 0.07] | 0.00 (0.10) |
| neg=H_high | C_msg | OW | 0.039 [0.00, 0.13] | 0.00 (0.10) |
| neg=H_high | C_msg | OWcal | 0.117 [0.03, 0.23] | 0.00 (0.10) |
| neg=H_high | C_msg | OWcal_hold | 0.927 [0.84, 0.99] | 0.90 (0.10) |
| neg=H_high | C_full | M | 0.029 [0.00, 0.10] | 0.00 (0.05) |
| neg=H_high | C_full | A | 0.114 [0.03, 0.22] | 0.00 (0.10) |
| neg=H_high | C_full | idx_last3 | 0.993 [0.97, 1.00] | 1.00 (0.10) |
| neg=H_high | C_full | hold_rate | 0.936 [0.85, 0.99] | 0.75 (0.10) |
| neg=H_high | C_full | C | 0.020 [0.00, 0.07] | 0.00 (0.10) |
| neg=H_high | C_full | S | 0.015 [0.00, 0.05] | 0.00 (0.10) |
| neg=H_high | C_full | OW | 0.025 [0.00, 0.09] | 0.00 (0.10) |
| neg=H_high | C_full | OWcal | 0.025 [0.00, 0.09] | 0.00 (0.10) |
| neg=H_high | C_full | OWcal_hold | 0.858 [0.73, 0.96] | 0.60 (0.10) |
| neg=H_high | C_adapt | M | 0.003 [0.00, 0.01] | 0.00 (0.05) |
| neg=H_high | C_adapt | A | 0.224 [0.10, 0.39] | 0.00 (0.10) |
| neg=H_high | C_adapt | idx_last3 | 0.868 [0.74, 0.96] | 0.75 (0.10) |
| neg=H_high | C_adapt | hold_rate | 0.573 [0.39, 0.76] | 0.00 (0.10) |
| neg=H_high | C_adapt | C | 0.020 [0.00, 0.07] | 0.00 (0.10) |
| neg=H_high | C_adapt | S | 0.001 [0.00, 0.01] | 0.00 (0.10) |
| neg=H_high | C_adapt | OW | 0.028 [0.00, 0.09] | 0.00 (0.10) |
| neg=H_high | C_adapt | OWcal | 0.075 [0.01, 0.17] | 0.00 (0.10) |
| neg=H_high | C_adapt | OWcal_hold | 0.440 [0.27, 0.62] | 0.00 (0.10) |
| neg=H_high | C_price | M | 0.005 [0.00, 0.02] | 0.00 (0.05) |
| neg=H_high | C_price | A | 0.206 [0.09, 0.36] | 0.00 (0.10) |
| neg=H_high | C_price | idx_last3 | 0.370 [0.20, 0.54] | 0.15 (0.10) |
| neg=H_high | C_price | hold_rate | 0.416 [0.24, 0.60] | 0.00 (0.10) |
| neg=H_high | C_price | C | 0.021 [0.00, 0.08] | 0.00 (0.10) |
| neg=H_high | C_price | S | 0.005 [0.00, 0.02] | 0.00 (0.10) |
| neg=H_high | C_price | OW | 0.026 [0.00, 0.09] | 0.00 (0.10) |
| neg=H_high | C_price | OWcal | 0.052 [0.00, 0.13] | 0.00 (0.10) |
| neg=H_high | C_price | OWcal_hold | 0.247 [0.11, 0.41] | 0.00 (0.10) |
| neg=H_high | pooled | M | 0.209 [0.13, 0.29] | 0.20 (0.05) |
| neg=H_high | pooled | A | 0.268 [0.17, 0.38] | 0.02 (0.10) |
| neg=H_high | pooled | idx_last3 | 0.832 [0.75, 0.90] | 0.76 (0.10) |
| neg=H_high | pooled | hold_rate | 0.781 [0.70, 0.87] | 0.54 (0.10) |
| neg=H_high | pooled | C | 0.219 [0.14, 0.31] | 0.20 (0.10) |
| neg=H_high | pooled | S | 0.208 [0.13, 0.29] | 0.20 (0.10) |
| neg=H_high | pooled | OW | 0.224 [0.14, 0.31] | 0.20 (0.10) |
| neg=H_high | pooled | OWcal | 0.244 [0.16, 0.33] | 0.20 (0.10) |
| neg=H_high | pooled | OWcal_hold | 0.684 [0.57, 0.79] | 0.50 (0.10) |
| neg=H_comp | C_naive | M | 1.000 [1.00, 1.00] | 1.00 (0.05) |
| neg=H_comp | C_naive | A | 0.610 [0.43, 0.78] | 0.20 (0.00) |
| neg=H_comp | C_naive | idx_last3 | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_naive | hold_rate | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_naive | C | 1.000 [1.00, 1.00] | 1.00 (0.05) |
| neg=H_comp | C_naive | S | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_naive | OW | 1.000 [1.00, 1.00] | 1.00 (0.05) |
| neg=H_comp | C_naive | OWcal | 1.000 [1.00, 1.00] | 1.00 (0.00) |
| neg=H_comp | C_naive | OWcal_hold | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_msg | M | 0.393 [0.22, 0.58] | 0.00 (0.05) |
| neg=H_comp | C_msg | A | 0.509 [0.33, 0.69] | 0.00 (0.00) |
| neg=H_comp | C_msg | idx_last3 | 0.990 [0.96, 1.00] | 0.95 (0.10) |
| neg=H_comp | C_msg | hold_rate | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_msg | C | 0.318 [0.17, 0.50] | 0.00 (0.05) |
| neg=H_comp | C_msg | S | 0.359 [0.20, 0.55] | 0.00 (0.10) |
| neg=H_comp | C_msg | OW | 0.233 [0.10, 0.39] | 0.00 (0.05) |
| neg=H_comp | C_msg | OWcal | 0.375 [0.21, 0.55] | 0.00 (0.00) |
| neg=H_comp | C_msg | OWcal_hold | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_full | M | 0.450 [0.26, 0.65] | 0.00 (0.05) |
| neg=H_comp | C_full | A | 0.315 [0.16, 0.48] | 0.00 (0.00) |
| neg=H_comp | C_full | idx_last3 | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_full | hold_rate | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_full | C | 0.216 [0.09, 0.37] | 0.00 (0.05) |
| neg=H_comp | C_full | S | 0.320 [0.15, 0.50] | 0.00 (0.10) |
| neg=H_comp | C_full | OW | 0.085 [0.01, 0.19] | 0.00 (0.05) |
| neg=H_comp | C_full | OWcal | 0.165 [0.06, 0.30] | 0.00 (0.00) |
| neg=H_comp | C_full | OWcal_hold | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_adapt | M | 0.125 [0.04, 0.24] | 0.00 (0.05) |
| neg=H_comp | C_adapt | A | 0.367 [0.20, 0.55] | 0.00 (0.00) |
| neg=H_comp | C_adapt | idx_last3 | 0.965 [0.91, 1.00] | 0.85 (0.10) |
| neg=H_comp | C_adapt | hold_rate | 0.836 [0.70, 0.95] | 0.70 (0.10) |
| neg=H_comp | C_adapt | C | 0.186 [0.07, 0.33] | 0.00 (0.05) |
| neg=H_comp | C_adapt | S | 0.153 [0.05, 0.28] | 0.00 (0.10) |
| neg=H_comp | C_adapt | OW | 0.130 [0.04, 0.25] | 0.00 (0.05) |
| neg=H_comp | C_adapt | OWcal | 0.245 [0.11, 0.41] | 0.00 (0.00) |
| neg=H_comp | C_adapt | OWcal_hold | 0.815 [0.66, 0.94] | 0.70 (0.10) |
| neg=H_comp | C_price | M | 0.133 [0.04, 0.25] | 0.00 (0.05) |
| neg=H_comp | C_price | A | 0.361 [0.20, 0.55] | 0.00 (0.00) |
| neg=H_comp | C_price | idx_last3 | 0.708 [0.56, 0.86] | 0.20 (0.10) |
| neg=H_comp | C_price | hold_rate | 0.691 [0.52, 0.84] | 0.30 (0.10) |
| neg=H_comp | C_price | C | 0.189 [0.06, 0.34] | 0.00 (0.05) |
| neg=H_comp | C_price | S | 0.170 [0.06, 0.31] | 0.00 (0.10) |
| neg=H_comp | C_price | OW | 0.113 [0.03, 0.22] | 0.00 (0.05) |
| neg=H_comp | C_price | OWcal | 0.235 [0.10, 0.40] | 0.00 (0.00) |
| neg=H_comp | C_price | OWcal_hold | 0.662 [0.48, 0.83] | 0.30 (0.10) |
| neg=H_comp | pooled | M | 0.420 [0.31, 0.53] | 0.20 (0.05) |
| neg=H_comp | pooled | A | 0.432 [0.30, 0.57] | 0.04 (0.00) |
| neg=H_comp | pooled | idx_last3 | 0.932 [0.88, 0.97] | 0.80 (0.10) |
| neg=H_comp | pooled | hold_rate | 0.905 [0.85, 0.95] | 0.80 (0.10) |
| neg=H_comp | pooled | C | 0.382 [0.26, 0.50] | 0.20 (0.05) |
| neg=H_comp | pooled | S | 0.400 [0.28, 0.52] | 0.20 (0.10) |
| neg=H_comp | pooled | OW | 0.312 [0.22, 0.41] | 0.20 (0.05) |
| neg=H_comp | pooled | OWcal | 0.404 [0.30, 0.51] | 0.20 (0.00) |
| neg=H_comp | pooled | OWcal_hold | 0.895 [0.84, 0.94] | 0.80 (0.10) |

| positives | difference | delta AUROC [95% CI] |
|---|---|---|
| C_naive | C - A | +0.463 [+0.31, +0.63] |
| C_naive | C - M | +0.004 [+0.00, +0.02] |
| C_naive | S - C | +0.000 [+0.00, +0.00] |
| C_naive | OW - C | +0.000 [+0.00, +0.00] |
| C_naive | OW - A | +0.463 [+0.31, +0.62] |
| C_naive | C - hold_rate | +0.000 [+0.00, +0.00] |
| C_naive | OWcal_hold - C | -0.025 [-0.06, +0.00] |
| C_msg | C - A | -0.247 [-0.43, -0.07] |
| C_msg | C - M | -0.031 [-0.10, +0.03] |
| C_msg | S - C | +0.014 [-0.04, +0.07] |
| C_msg | OW - C | -0.039 [-0.10, +0.02] |
| C_msg | OW - A | -0.286 [-0.44, -0.14] |
| C_msg | C - hold_rate | -0.816 [-0.91, -0.71] |
| C_msg | OWcal_hold - C | +0.789 [+0.67, +0.88] |
| C_full | C - A | -0.096 [-0.25, +0.06] |
| C_full | C - M | -0.121 [-0.21, -0.06] |
| C_full | S - C | +0.049 [-0.01, +0.12] |
| C_full | OW - C | -0.063 [-0.14, -0.01] |
| C_full | OW - A | -0.159 [-0.29, -0.05] |
| C_full | C - hold_rate | -0.850 [-0.93, -0.75] |
| C_full | OWcal_hold - C | +0.811 [+0.70, +0.90] |
| C_adapt | C - A | -0.192 [-0.37, -0.03] |
| C_adapt | C - M | +0.039 [-0.01, +0.10] |
| C_adapt | S - C | -0.026 [-0.08, +0.03] |
| C_adapt | OW - C | -0.024 [-0.08, +0.03] |
| C_adapt | OW - A | -0.217 [-0.36, -0.09] |
| C_adapt | C - hold_rate | -0.601 [-0.74, -0.45] |
| C_adapt | OWcal_hold - C | +0.524 [+0.37, +0.67] |
| C_price | C - A | -0.179 [-0.35, -0.02] |
| C_price | C - M | +0.036 [-0.01, +0.09] |
| C_price | S - C | -0.018 [-0.07, +0.02] |
| C_price | OW - C | -0.036 [-0.10, +0.02] |
| C_price | OW - A | -0.214 [-0.35, -0.09] |
| C_price | C - hold_rate | -0.449 [-0.59, -0.29] |
| C_price | OWcal_hold - C | +0.350 [+0.21, +0.49] |
| pooled | C - A | -0.050 [-0.18, +0.07] |
| pooled | C - M | -0.015 [-0.05, +0.02] |
| pooled | S - C | +0.004 [-0.03, +0.04] |
| pooled | OW - C | -0.032 [-0.08, +0.01] |
| pooled | OW - A | -0.083 [-0.19, +0.02] |
| pooled | C - hold_rate | -0.543 [-0.63, -0.45] |
| pooled | OWcal_hold - C | +0.490 [+0.40, +0.58] |

| detector (threshold) | H_comp | H_high | C_naive | C_msg | C_full | C_adapt | C_price | accuracy |
|---|---|---|---|---|---|---|---|---|
| M (>= 50) | 0.60 | 1.00 | 1.00 | 0.65 | 0.70 | 0.15 | 0.10 | 0.43 |
| A (>= 50) | 0.60 | 0.95 | 0.85 | 0.65 | 0.40 | 0.45 | 0.45 | 0.46 |
| C (>= 50) | 0.70 | 0.95 | 1.00 | 0.60 | 0.25 | 0.30 | 0.15 | 0.38 |
| S (>= 50) | 0.75 | 1.00 | 1.00 | 0.70 | 0.80 | 0.35 | 0.25 | 0.48 |
| OW (>= 50) | 1.00 | 1.00 | 1.00 | 0.80 | 0.65 | 0.60 | 0.55 | 0.51 |
| hold_rate (>= 0.5) | 0.00 | 0.20 | 1.00 | 0.95 | 0.95 | 0.05 | 0.10 | 0.69 |

| arm | n | M | A | idx_last3 | hold_rate | C | S | OW | OWcal | OWcal_hold | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H_comp | 20 | 62.70 | 55.55 | 0.51 | 0.15 | 66.25 | 69.50 | 76.40 | 0.53 | 0.43 | -10.70 |
| H_high | 20 | 92.85 | 65.60 | 0.62 | 0.30 | 91.55 | 94.05 | 92.40 | 0.82 | 0.78 | -25.95 |
| C_naive | 20 | 99.65 | 62.50 | 0.73 | 0.93 | 99.60 | 99.25 | 99.60 | 1.00 | 1.00 | -37.10 |
| C_msg | 20 | 55.50 | 56.25 | 0.72 | 0.78 | 53.80 | 60.95 | 62.95 | 0.45 | 0.99 | 2.45 |
| C_full | 20 | 59.60 | 46.50 | 0.73 | 0.69 | 41.55 | 60.50 | 53.80 | 0.26 | 0.97 | 4.95 |
| C_adapt | 20 | 30.65 | 48.75 | 0.68 | 0.33 | 40.40 | 41.30 | 53.95 | 0.32 | 0.70 | 8.35 |
| C_price | 20 | 33.50 | 48.60 | 0.60 | 0.24 | 37.50 | 41.75 | 52.40 | 0.31 | 0.56 | 11.10 |
