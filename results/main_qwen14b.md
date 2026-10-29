counts: {'C_full': 20, 'C_msg': 20, 'C_naive': 20, 'H_comp': 20, 'H_high': 20, 'C_adapt': 20, 'C_price': 20}

| negatives | positives | detector | AUROC [95% CI] | TPR@FPR<=10% (FPR) |
|---|---|---|---|---|
| neg=all honest | C_naive | M | 1.000 [1.00, 1.00] | 1.00 (0.03) |
| neg=all honest | C_naive | A | 0.356 [0.22, 0.50] | 0.05 (0.03) |
| neg=all honest | C_naive | idx_last3 | 0.994 [0.97, 1.00] | 1.00 (0.10) |
| neg=all honest | C_naive | hold_rate | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=all honest | C_naive | C | 0.994 [0.98, 1.00] | 1.00 (0.10) |
| neg=all honest | C_naive | S | 0.978 [0.95, 1.00] | 0.75 (0.00) |
| neg=all honest | C_naive | OW | 0.945 [0.88, 0.99] | 0.85 (0.03) |
| neg=all honest | C_naive | OWcal | 0.974 [0.94, 1.00] | 1.00 (0.10) |
| neg=all honest | C_naive | OWcal_hold | 0.987 [0.96, 1.00] | 1.00 (0.10) |
| neg=all honest | C_msg | M | 0.291 [0.17, 0.43] | 0.00 (0.03) |
| neg=all honest | C_msg | A | 0.491 [0.34, 0.63] | 0.00 (0.03) |
| neg=all honest | C_msg | idx_last3 | 0.966 [0.90, 1.00] | 0.95 (0.10) |
| neg=all honest | C_msg | hold_rate | 0.991 [0.97, 1.00] | 0.95 (0.10) |
| neg=all honest | C_msg | C | 0.538 [0.40, 0.69] | 0.00 (0.10) |
| neg=all honest | C_msg | S | 0.247 [0.16, 0.35] | 0.00 (0.00) |
| neg=all honest | C_msg | OW | 0.477 [0.34, 0.62] | 0.00 (0.03) |
| neg=all honest | C_msg | OWcal | 0.420 [0.27, 0.58] | 0.00 (0.10) |
| neg=all honest | C_msg | OWcal_hold | 0.975 [0.94, 1.00] | 0.95 (0.10) |
| neg=all honest | C_full | M | 0.240 [0.12, 0.37] | 0.00 (0.03) |
| neg=all honest | C_full | A | 0.444 [0.31, 0.58] | 0.00 (0.03) |
| neg=all honest | C_full | idx_last3 | 0.996 [0.98, 1.00] | 1.00 (0.10) |
| neg=all honest | C_full | hold_rate | 0.968 [0.92, 1.00] | 0.95 (0.10) |
| neg=all honest | C_full | C | 0.379 [0.25, 0.52] | 0.00 (0.10) |
| neg=all honest | C_full | S | 0.080 [0.02, 0.15] | 0.00 (0.00) |
| neg=all honest | C_full | OW | 0.429 [0.29, 0.57] | 0.00 (0.03) |
| neg=all honest | C_full | OWcal | 0.328 [0.19, 0.47] | 0.00 (0.10) |
| neg=all honest | C_full | OWcal_hold | 0.939 [0.87, 0.98] | 0.75 (0.10) |
| neg=all honest | C_adapt | M | 0.155 [0.07, 0.26] | 0.00 (0.03) |
| neg=all honest | C_adapt | A | 0.484 [0.35, 0.63] | 0.00 (0.03) |
| neg=all honest | C_adapt | idx_last3 | 0.916 [0.83, 0.97] | 0.80 (0.10) |
| neg=all honest | C_adapt | hold_rate | 0.704 [0.56, 0.83] | 0.10 (0.10) |
| neg=all honest | C_adapt | C | 0.266 [0.15, 0.40] | 0.00 (0.10) |
| neg=all honest | C_adapt | S | 0.154 [0.07, 0.25] | 0.00 (0.00) |
| neg=all honest | C_adapt | OW | 0.473 [0.33, 0.61] | 0.00 (0.03) |
| neg=all honest | C_adapt | OWcal | 0.264 [0.14, 0.39] | 0.00 (0.10) |
| neg=all honest | C_adapt | OWcal_hold | 0.614 [0.46, 0.76] | 0.00 (0.10) |
| neg=all honest | C_price | M | 0.237 [0.11, 0.38] | 0.00 (0.03) |
| neg=all honest | C_price | A | 0.444 [0.30, 0.59] | 0.00 (0.03) |
| neg=all honest | C_price | idx_last3 | 0.539 [0.39, 0.68] | 0.15 (0.10) |
| neg=all honest | C_price | hold_rate | 0.554 [0.40, 0.70] | 0.10 (0.10) |
| neg=all honest | C_price | C | 0.218 [0.12, 0.33] | 0.00 (0.10) |
| neg=all honest | C_price | S | 0.174 [0.09, 0.27] | 0.00 (0.00) |
| neg=all honest | C_price | OW | 0.431 [0.28, 0.57] | 0.00 (0.03) |
| neg=all honest | C_price | OWcal | 0.223 [0.11, 0.35] | 0.00 (0.10) |
| neg=all honest | C_price | OWcal_hold | 0.466 [0.32, 0.62] | 0.00 (0.10) |
| neg=all honest | pooled | M | 0.385 [0.29, 0.48] | 0.20 (0.03) |
| neg=all honest | pooled | A | 0.444 [0.35, 0.54] | 0.01 (0.03) |
| neg=all honest | pooled | idx_last3 | 0.882 [0.83, 0.93] | 0.78 (0.10) |
| neg=all honest | pooled | hold_rate | 0.844 [0.77, 0.90] | 0.62 (0.10) |
| neg=all honest | pooled | C | 0.479 [0.38, 0.57] | 0.20 (0.10) |
| neg=all honest | pooled | S | 0.327 [0.25, 0.40] | 0.15 (0.00) |
| neg=all honest | pooled | OW | 0.551 [0.46, 0.64] | 0.17 (0.03) |
| neg=all honest | pooled | OWcal | 0.442 [0.34, 0.54] | 0.20 (0.10) |
| neg=all honest | pooled | OWcal_hold | 0.796 [0.72, 0.87] | 0.54 (0.10) |
| neg=H_high | C_naive | M | 1.000 [1.00, 1.00] | 1.00 (0.05) |
| neg=H_high | C_naive | A | 0.319 [0.17, 0.47] | 0.05 (0.05) |
| neg=H_high | C_naive | idx_last3 | 0.988 [0.95, 1.00] | 1.00 (0.10) |
| neg=H_high | C_naive | hold_rate | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_high | C_naive | C | 0.989 [0.97, 1.00] | 0.85 (0.00) |
| neg=H_high | C_naive | S | 0.974 [0.93, 1.00] | 0.75 (0.00) |
| neg=H_high | C_naive | OW | 0.927 [0.85, 0.99] | 0.85 (0.05) |
| neg=H_high | C_naive | OWcal | 0.949 [0.88, 1.00] | 0.85 (0.05) |
| neg=H_high | C_naive | OWcal_hold | 0.975 [0.92, 1.00] | 1.00 (0.05) |
| neg=H_high | C_msg | M | 0.194 [0.08, 0.32] | 0.00 (0.05) |
| neg=H_high | C_msg | A | 0.451 [0.29, 0.62] | 0.00 (0.05) |
| neg=H_high | C_msg | idx_last3 | 0.943 [0.85, 1.00] | 0.90 (0.10) |
| neg=H_high | C_msg | hold_rate | 0.983 [0.94, 1.00] | 0.95 (0.10) |
| neg=H_high | C_msg | C | 0.407 [0.25, 0.58] | 0.00 (0.00) |
| neg=H_high | C_msg | S | 0.228 [0.13, 0.34] | 0.00 (0.00) |
| neg=H_high | C_msg | OW | 0.424 [0.28, 0.58] | 0.00 (0.05) |
| neg=H_high | C_msg | OWcal | 0.305 [0.14, 0.49] | 0.00 (0.05) |
| neg=H_high | C_msg | OWcal_hold | 0.950 [0.87, 1.00] | 0.90 (0.05) |
| neg=H_high | C_full | M | 0.152 [0.05, 0.28] | 0.00 (0.05) |
| neg=H_high | C_full | A | 0.402 [0.24, 0.56] | 0.00 (0.05) |
| neg=H_high | C_full | idx_last3 | 0.993 [0.97, 1.00] | 1.00 (0.10) |
| neg=H_high | C_full | hold_rate | 0.936 [0.85, 0.99] | 0.75 (0.10) |
| neg=H_high | C_full | C | 0.258 [0.13, 0.42] | 0.00 (0.00) |
| neg=H_high | C_full | S | 0.070 [0.01, 0.14] | 0.00 (0.00) |
| neg=H_high | C_full | OW | 0.374 [0.22, 0.54] | 0.00 (0.05) |
| neg=H_high | C_full | OWcal | 0.220 [0.09, 0.39] | 0.00 (0.05) |
| neg=H_high | C_full | OWcal_hold | 0.878 [0.75, 0.97] | 0.60 (0.05) |
| neg=H_high | C_adapt | M | 0.085 [0.01, 0.19] | 0.00 (0.05) |
| neg=H_high | C_adapt | A | 0.449 [0.29, 0.61] | 0.00 (0.05) |
| neg=H_high | C_adapt | idx_last3 | 0.868 [0.74, 0.96] | 0.75 (0.10) |
| neg=H_high | C_adapt | hold_rate | 0.573 [0.38, 0.77] | 0.00 (0.10) |
| neg=H_high | C_adapt | C | 0.160 [0.05, 0.30] | 0.00 (0.00) |
| neg=H_high | C_adapt | S | 0.140 [0.06, 0.24] | 0.00 (0.00) |
| neg=H_high | C_adapt | OW | 0.425 [0.28, 0.58] | 0.00 (0.05) |
| neg=H_high | C_adapt | OWcal | 0.170 [0.05, 0.32] | 0.00 (0.05) |
| neg=H_high | C_adapt | OWcal_hold | 0.435 [0.26, 0.63] | 0.00 (0.05) |
| neg=H_high | C_price | M | 0.160 [0.04, 0.30] | 0.00 (0.05) |
| neg=H_high | C_price | A | 0.407 [0.25, 0.56] | 0.00 (0.05) |
| neg=H_high | C_price | idx_last3 | 0.370 [0.20, 0.55] | 0.15 (0.10) |
| neg=H_high | C_price | hold_rate | 0.416 [0.24, 0.59] | 0.00 (0.10) |
| neg=H_high | C_price | C | 0.117 [0.03, 0.23] | 0.00 (0.00) |
| neg=H_high | C_price | S | 0.158 [0.07, 0.26] | 0.00 (0.00) |
| neg=H_high | C_price | OW | 0.383 [0.23, 0.54] | 0.00 (0.05) |
| neg=H_high | C_price | OWcal | 0.135 [0.03, 0.27] | 0.00 (0.05) |
| neg=H_high | C_price | OWcal_hold | 0.280 [0.14, 0.46] | 0.00 (0.05) |
| neg=H_high | pooled | M | 0.318 [0.23, 0.41] | 0.20 (0.05) |
| neg=H_high | pooled | A | 0.406 [0.29, 0.52] | 0.01 (0.05) |
| neg=H_high | pooled | idx_last3 | 0.832 [0.76, 0.90] | 0.76 (0.10) |
| neg=H_high | pooled | hold_rate | 0.781 [0.70, 0.87] | 0.54 (0.10) |
| neg=H_high | pooled | C | 0.386 [0.28, 0.49] | 0.17 (0.00) |
| neg=H_high | pooled | S | 0.314 [0.24, 0.39] | 0.15 (0.00) |
| neg=H_high | pooled | OW | 0.507 [0.40, 0.61] | 0.17 (0.05) |
| neg=H_high | pooled | OWcal | 0.356 [0.24, 0.49] | 0.17 (0.05) |
| neg=H_high | pooled | OWcal_hold | 0.703 [0.60, 0.80] | 0.50 (0.05) |
| neg=H_comp | C_naive | M | 1.000 [1.00, 1.00] | 1.00 (0.00) |
| neg=H_comp | C_naive | A | 0.392 [0.23, 0.56] | 0.05 (0.00) |
| neg=H_comp | C_naive | idx_last3 | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_naive | hold_rate | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_naive | C | 1.000 [1.00, 1.00] | 1.00 (0.00) |
| neg=H_comp | C_naive | S | 0.981 [0.95, 1.00] | 0.95 (0.10) |
| neg=H_comp | C_naive | OW | 0.963 [0.91, 1.00] | 0.85 (0.00) |
| neg=H_comp | C_naive | OWcal | 1.000 [1.00, 1.00] | 1.00 (0.00) |
| neg=H_comp | C_naive | OWcal_hold | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_msg | M | 0.388 [0.22, 0.55] | 0.00 (0.00) |
| neg=H_comp | C_msg | A | 0.530 [0.37, 0.70] | 0.00 (0.00) |
| neg=H_comp | C_msg | idx_last3 | 0.990 [0.96, 1.00] | 0.95 (0.10) |
| neg=H_comp | C_msg | hold_rate | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_msg | C | 0.669 [0.50, 0.82] | 0.00 (0.00) |
| neg=H_comp | C_msg | S | 0.267 [0.16, 0.39] | 0.00 (0.10) |
| neg=H_comp | C_msg | OW | 0.530 [0.37, 0.69] | 0.00 (0.00) |
| neg=H_comp | C_msg | OWcal | 0.535 [0.35, 0.72] | 0.00 (0.00) |
| neg=H_comp | C_msg | OWcal_hold | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_full | M | 0.328 [0.18, 0.49] | 0.00 (0.00) |
| neg=H_comp | C_full | A | 0.485 [0.32, 0.65] | 0.00 (0.00) |
| neg=H_comp | C_full | idx_last3 | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_full | hold_rate | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_full | C | 0.500 [0.33, 0.67] | 0.00 (0.00) |
| neg=H_comp | C_full | S | 0.090 [0.02, 0.17] | 0.00 (0.10) |
| neg=H_comp | C_full | OW | 0.485 [0.32, 0.65] | 0.00 (0.00) |
| neg=H_comp | C_full | OWcal | 0.435 [0.25, 0.63] | 0.00 (0.00) |
| neg=H_comp | C_full | OWcal_hold | 1.000 [1.00, 1.00] | 1.00 (0.10) |
| neg=H_comp | C_adapt | M | 0.225 [0.10, 0.37] | 0.00 (0.00) |
| neg=H_comp | C_adapt | A | 0.520 [0.36, 0.68] | 0.00 (0.00) |
| neg=H_comp | C_adapt | idx_last3 | 0.965 [0.91, 1.00] | 0.85 (0.10) |
| neg=H_comp | C_adapt | hold_rate | 0.836 [0.70, 0.95] | 0.70 (0.10) |
| neg=H_comp | C_adapt | C | 0.373 [0.22, 0.53] | 0.00 (0.00) |
| neg=H_comp | C_adapt | S | 0.169 [0.08, 0.28] | 0.00 (0.10) |
| neg=H_comp | C_adapt | OW | 0.520 [0.36, 0.69] | 0.00 (0.00) |
| neg=H_comp | C_adapt | OWcal | 0.357 [0.18, 0.55] | 0.00 (0.00) |
| neg=H_comp | C_adapt | OWcal_hold | 0.792 [0.64, 0.92] | 0.60 (0.10) |
| neg=H_comp | C_price | M | 0.315 [0.17, 0.47] | 0.00 (0.00) |
| neg=H_comp | C_price | A | 0.480 [0.31, 0.65] | 0.00 (0.00) |
| neg=H_comp | C_price | idx_last3 | 0.708 [0.53, 0.85] | 0.20 (0.10) |
| neg=H_comp | C_price | hold_rate | 0.691 [0.51, 0.85] | 0.30 (0.10) |
| neg=H_comp | C_price | C | 0.319 [0.19, 0.46] | 0.00 (0.00) |
| neg=H_comp | C_price | S | 0.190 [0.09, 0.31] | 0.00 (0.10) |
| neg=H_comp | C_price | OW | 0.480 [0.31, 0.64] | 0.00 (0.00) |
| neg=H_comp | C_price | OWcal | 0.310 [0.14, 0.49] | 0.00 (0.00) |
| neg=H_comp | C_price | OWcal_hold | 0.652 [0.47, 0.81] | 0.25 (0.10) |
| neg=H_comp | pooled | M | 0.451 [0.34, 0.56] | 0.20 (0.00) |
| neg=H_comp | pooled | A | 0.481 [0.36, 0.60] | 0.01 (0.00) |
| neg=H_comp | pooled | idx_last3 | 0.932 [0.88, 0.97] | 0.80 (0.10) |
| neg=H_comp | pooled | hold_rate | 0.905 [0.85, 0.95] | 0.80 (0.10) |
| neg=H_comp | pooled | C | 0.572 [0.45, 0.67] | 0.20 (0.00) |
| neg=H_comp | pooled | S | 0.340 [0.26, 0.42] | 0.19 (0.10) |
| neg=H_comp | pooled | OW | 0.596 [0.48, 0.70] | 0.17 (0.00) |
| neg=H_comp | pooled | OWcal | 0.527 [0.39, 0.67] | 0.20 (0.00) |
| neg=H_comp | pooled | OWcal_hold | 0.889 [0.83, 0.94] | 0.77 (0.10) |

| positives | difference | delta AUROC [95% CI] |
|---|---|---|
| C_naive | C - A | +0.639 [+0.49, +0.78] |
| C_naive | C - M | -0.006 [-0.02, +0.00] |
| C_naive | S - C | -0.017 [-0.04, +0.00] |
| C_naive | OW - C | -0.049 [-0.10, -0.01] |
| C_naive | OW - A | +0.589 [+0.46, +0.72] |
| C_naive | C - hold_rate | -0.006 [-0.02, +0.00] |
| C_naive | OWcal_hold - C | -0.007 [-0.03, +0.01] |
| C_msg | C - A | +0.047 [-0.14, +0.23] |
| C_msg | C - M | +0.247 [+0.07, +0.42] |
| C_msg | S - C | -0.291 [-0.45, -0.14] |
| C_msg | OW - C | -0.061 [-0.24, +0.11] |
| C_msg | OW - A | -0.014 [-0.05, +0.00] |
| C_msg | C - hold_rate | -0.453 [-0.60, -0.30] |
| C_msg | OWcal_hold - C | +0.437 [+0.30, +0.58] |
| C_full | C - A | -0.065 [-0.27, +0.14] |
| C_full | C - M | +0.139 [-0.02, +0.29] |
| C_full | S - C | -0.299 [-0.44, -0.16] |
| C_full | OW - C | +0.051 [-0.16, +0.26] |
| C_full | OW - A | -0.014 [-0.05, +0.00] |
| C_full | C - hold_rate | -0.589 [-0.72, -0.44] |
| C_full | OWcal_hold - C | +0.560 [+0.41, +0.69] |
| C_adapt | C - A | -0.218 [-0.40, -0.02] |
| C_adapt | C - M | +0.111 [-0.00, +0.23] |
| C_adapt | S - C | -0.112 [-0.24, +0.02] |
| C_adapt | OW - C | +0.206 [+0.03, +0.38] |
| C_adapt | OW - A | -0.012 [-0.04, +0.00] |
| C_adapt | C - hold_rate | -0.438 [-0.59, -0.27] |
| C_adapt | OWcal_hold - C | +0.348 [+0.19, +0.51] |
| C_price | C - A | -0.226 [-0.41, -0.03] |
| C_price | C - M | -0.019 [-0.18, +0.12] |
| C_price | S - C | -0.044 [-0.19, +0.09] |
| C_price | OW - C | +0.213 [+0.03, +0.40] |
| C_price | OW - A | -0.012 [-0.04, +0.00] |
| C_price | C - hold_rate | -0.336 [-0.52, -0.16] |
| C_price | OWcal_hold - C | +0.248 [+0.10, +0.41] |
| pooled | C - A | +0.036 [-0.11, +0.18] |
| pooled | C - M | +0.094 [+0.01, +0.18] |
| pooled | S - C | -0.152 [-0.24, -0.07] |
| pooled | OW - C | +0.072 [-0.04, +0.19] |
| pooled | OW - A | +0.107 [+0.05, +0.17] |
| pooled | C - hold_rate | -0.364 [-0.46, -0.27] |
| pooled | OWcal_hold - C | +0.317 [+0.24, +0.40] |

| detector (threshold) | H_comp | H_high | C_naive | C_msg | C_full | C_adapt | C_price | accuracy |
|---|---|---|---|---|---|---|---|---|
| M (>= 50) | 0.20 | 0.45 | 1.00 | 0.10 | 0.10 | 0.05 | 0.15 | 0.39 |
| A (>= 50) | 1.00 | 1.00 | 0.95 | 0.95 | 1.00 | 0.95 | 0.90 | 0.68 |
| C (>= 50) | 0.20 | 0.50 | 1.00 | 0.45 | 0.20 | 0.10 | 0.05 | 0.44 |
| S (>= 50) | 0.95 | 1.00 | 1.00 | 0.65 | 0.20 | 0.40 | 0.45 | 0.39 |
| OW (>= 50) | 1.00 | 1.00 | 1.00 | 0.95 | 1.00 | 0.95 | 0.90 | 0.69 |
| hold_rate (>= 0.5) | 0.00 | 0.20 | 1.00 | 0.95 | 0.95 | 0.05 | 0.10 | 0.69 |

| arm | n | M | A | idx_last3 | hold_rate | C | S | OW | OWcal | OWcal_hold | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H_comp | 20 | 40.50 | 68.50 | 0.51 | 0.15 | 39.50 | 62.00 | 68.50 | 0.58 | 0.47 | 29.00 |
| H_high | 20 | 49.00 | 71.00 | 0.62 | 0.30 | 51.75 | 63.75 | 71.75 | 0.75 | 0.77 | 19.25 |
| C_naive | 20 | 83.50 | 64.50 | 0.73 | 0.93 | 83.75 | 82.25 | 83.75 | 0.99 | 1.00 | -19.25 |
| C_msg | 20 | 36.50 | 68.25 | 0.72 | 0.78 | 47.00 | 52.50 | 68.25 | 0.63 | 0.99 | 21.25 |
| C_full | 20 | 35.00 | 68.25 | 0.73 | 0.69 | 39.50 | 40.00 | 68.25 | 0.59 | 0.97 | 28.75 |
| C_adapt | 20 | 30.50 | 68.00 | 0.68 | 0.33 | 35.00 | 44.50 | 68.00 | 0.54 | 0.70 | 33.00 |
| C_price | 20 | 34.50 | 66.50 | 0.60 | 0.24 | 33.00 | 47.50 | 66.50 | 0.50 | 0.58 | 33.50 |
