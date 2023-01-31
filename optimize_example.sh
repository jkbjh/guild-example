guild run -y op_optimize method=ABSMIN a=1 b=1

guild run -y op_optimize method="EASOM" x="[0.:2.]" y="[0.:2.]"  --optimizer=random --minimize loss --max-trials 5  -t optimize_runs

guild run -y op_optimize method="EASOM" x="[0.:2.]" y="[0.:2.]"  --optimizer=gp  --minimize loss --max-trials 5  -t optimize_runs
