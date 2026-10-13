import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import numpy as np

    def cyclical_encoding(x_values, cycle_max=None):
        x_max = cycle_max or x_values.max()
        x_sin = np.sin(2 * np.pi * x_values / x_max)
        x_cos = np.cos(2 * np.pi * x_values / x_max)
        return x_sin, x_cos

    return


if __name__ == "__main__":
    app.run()
