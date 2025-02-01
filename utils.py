import base64
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def get_download_link(df: pd.DataFrame, filename: str, text: str) -> str:
    """
    Create a download link for a DataFrame as a CSV file.
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'

def create_3d_surface(P_range: np.ndarray, T_range: np.ndarray, deltaH: float, deltaS: float) -> go.Surface:
    """
    Generate a 3D surface plot of the adsorption isotherm.
    """
    P, T = np.meshgrid(P_range, T_range)
    K = np.exp((-deltaH * 1000) / (8.314 * T) + deltaS / 8.314)
    Q = (K * P) / (1 + K * P)
    return go.Surface(x=P, y=T, z=Q)

def langmuir_isotherm(pressures: np.ndarray, K: float) -> np.ndarray:
    """
    Compute the Langmuir isotherm.
    """
    return (K * pressures) / (1 + K * pressures)
