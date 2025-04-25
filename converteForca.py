import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os
import math

def processar_csv(input_csv, escala):
    # Lê nomes das colunas da primeira linha e os dados a partir da segunda
    with open(input_csv, 'r') as f:
        nomes_colunas = f.readline().strip().split(',')

    df = pd.read_csv(input_csv, skiprows=1, names=nomes_colunas)

    if "kalman_angle_roll" not in df.columns or "time" not in df.columns:
        raise ValueError("CSV precisa conter as colunas 'kalman_angle_roll' e 'time'.")
    
    #Conserta o erro dos ângulos
    df["kalman_angle_roll"] = df["kalman_angle_roll"]-df["kalman_angle_roll"].iloc[1]
    df["kalman_angle_roll"] = df["kalman_angle_roll"].abs()

    #Calcula a força (N)
    if escala == 50:
        df["Forca (N)"] = df["kalman_angle_roll"] * 0.03611 * 9.80665 #fazer testes pra achar as constantes certas
    elif escala == 100:
        df["Forca (N)"] = df["kalman_angle_roll"] * 0.09028 * 9.80665 #fazer testes pra achar as constantes certas
    elif escala == 200:
        df["Forca (N)"] = df["kalman_angle_roll"] * 0.18111 * 9.80665 #fazer testes pra achar as constantes certas
    else:
        raise ValueError("A escala utilizada é inválida.")

    # Seleciona colunas relevantes
    df_filtrado = df[["time", "Forca (N)"]]

    # Salva novo CSV
    output_csv = os.path.splitext(input_csv)[0] + "_transformado.csv"
    df_filtrado.to_csv(output_csv, index=False)
    print(f"Arquivo salvo como: {output_csv}")

    #Gera gráfico de força
    plt.figure(figsize=(10, 6))
    plt.plot(df_filtrado["Forca (N)"])
    plt.title("Força ao longo do tempo")
    plt.xlabel("Índice")
    plt.ylabel("Forca (N)")
    plt.grid(True)
    plt.savefig("grafico_forca.png")
    print("Gráfico salvo como: grafico_forca.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", help="Caminho para o arquivo CSV")
    parser.add_argument("--escala", type=int, help="Escala (kg)")

    args = parser.parse_args()
    escala = args.escala
    processar_csv(args.csv_file, escala)
