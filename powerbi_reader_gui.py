import requests
import msal
import tkinter as tk
from tkinter import messagebox

# Configuración de Azure AD
CLIENT_ID = 'tu-client-id'
TENANT_ID = 'tu-tenant-id'
CLIENT_SECRET = 'tu-client-secret'
AUTHORITY = f'https://login.microsoftonline.com/{TENANT_ID}'
SCOPE = ['https://analysis.windows.net/powerbi/api/.default']

BASE_URL = 'https://api.powerbi.com/v1.0/myorg/'

def get_access_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )
    result = app.acquire_token_for_client(scopes=SCOPE)
    if "access_token" in result:
        return result['access_token']
    else:
        raise Exception("No se pudo obtener el token de acceso.")

def get_dashboards(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(BASE_URL + 'dashboards', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_tiles_in_dashboard(token, dashboard_id):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(BASE_URL + f'dashboards/{dashboard_id}/tiles', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def display_dashboards():
    try:
        access_token = get_access_token()
        dashboards = get_dashboards(access_token)
        dashboard_list.delete(0, tk.END)
        for dashboard in dashboards['value']:
            dashboard_list.insert(tk.END, (dashboard['id'], dashboard['displayName']))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def display_tiles():
    try:
        selected_dashboard = dashboard_list.get(dashboard_list.curselection())
        dashboard_id = selected_dashboard[0]
        access_token = get_access_token()
        tiles = get_tiles_in_dashboard(access_token, dashboard_id)
        tiles_list.delete(0, tk.END)
        for tile in tiles['value']:
            tiles_list.insert(tk.END, tile['title'])
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Power BI Dashboard Reader")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Botón para obtener dashboards
btn_get_dashboards = tk.Button(frame, text="Obtener Dashboards", command=display_dashboards)
btn_get_dashboards.pack(fill=tk.X)

# Lista de dashboards
dashboard_list = tk.Listbox(frame)
dashboard_list.pack(fill=tk.BOTH, expand=True)

# Botón para obtener tiles del dashboard seleccionado
btn_get_tiles = tk.Button(frame, text="Obtener Tiles del Dashboard", command=display_tiles)
btn_get_tiles.pack(fill=tk.X)

# Lista de tiles
tiles_list = tk.Listbox(frame)
tiles_list.pack(fill=tk.BOTH, expand=True)

root.mainloop()
