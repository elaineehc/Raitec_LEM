import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os
import math

def calcular_area(diametro=None, area=None):
    if area:
        return float(area)
    elif diametro:
        return math.pi * (float(diametro) ** 2) / 4
    else:
        raise ValueError("Você precisa informar a área ou diâmetro.")


def processar_csv(input_csv, area, escala):
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
        df["Forca (N)"] = df["kalman_angle_roll"] * 1.80555 * 9.80665
    elif escala == 100:
        df["Forca (N)"] = df["kalman_angle_roll"] * 9.02777 * 9.80665
    else:
        raise ValueError("A escala utilizada é inválida.")

    # Calcula tensão
    df["Tensao (Pa)"] = df["Forca (N)"] / area

    # Seleciona colunas relevantes
    df_filtrado = df[["time", "Forca (N)", "Tensao (Pa)"]]

    # Salva novo CSV
    output_csv = os.path.splitext(input_csv)[0] + "_transformado.csv"
    df_filtrado.to_csv(output_csv, index=False)
    print(f"Arquivo salvo como: {output_csv}")

    # Gera gráfico de tensão
    plt.figure(figsize=(10, 6))
    plt.plot(df_filtrado["Tensao (Pa)"])
    plt.title("Tensão ao longo do tempo")
    plt.xlabel("Índice")
    plt.ylabel("Tensao (Pa)")
    plt.grid(True)
    plt.savefig("grafico_tensao.png")
    print("Gráfico salvo como: grafico_tensao.png")

    # Gera gráfico de força
    # plt.figure(figsize=(10, 6))
    # plt.plot(df_filtrado["Forca (N)"])
    # plt.title("Força ao longo do tempo")
    # plt.xlabel("Índice")
    # plt.ylabel("Forca (N)")
    # plt.grid(True)
    # plt.savefig("grafico_forca.png")
    # print("Gráfico salvo como: grafico_forca.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", help="Caminho para o arquivo CSV")
    parser.add_argument("--area", type=float, help="Área (m²)")
    parser.add_argument("--diametro", type=float, help="Diâmetro (m)")
    parser.add_argument("--escala", type=int, help="Escala (kg)")

    args = parser.parse_args()
    area = calcular_area(diametro=args.diametro, area=args.area)
    escala = args.escala
    processar_csv(args.csv_file, area, escala)
