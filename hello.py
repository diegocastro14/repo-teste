#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de exemplo para teste
"""

def saudacao(nome):
    """Função que retorna uma saudação personalizada"""
    return f"Olá, {nome}! Este é um repositório de teste."

def main():
    """Função principal"""
    nome = input("Digite seu nome: ")
    print(saudacao(nome))
    
    # Exemplo de operações matemáticas
    numeros = [1, 2, 3, 4, 5]
    soma = sum(numeros)
    print(f"A soma dos números {numeros} é: {soma}")

if __name__ == "__main__":
    main()
