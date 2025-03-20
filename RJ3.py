#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 00:22:15 2025

@author: momol
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# Barre latérale pour la navigation entre les pages
page = st.sidebar.radio("Navigation", ["Accueil", "Créanciers & Fournisseurs", "Solutions"])

# ========================
# PAGE 1 : Accueil - Informations Générales
# ========================
if page == "Accueil":
    st.title("Suivi du Redressement Judiciaire")

    # Informations client et expert
    st.write("### Client en redressement judiciaire : XXXX")
    st.write("### Expert-comptable : François DUPONT")

    # Procédures judiciaires envisageables
    st.write("### Procédures judiciaires envisageables")
    procedures = [
        "Sauvegarde judiciaire",
        "Redressement judiciaire",
        "Liquidation judiciaire",
        "Conciliation avec les créanciers",
        "Procédure de cession"
    ]
    for proc in procedures:
        st.write(f"- {proc}")

# ========================
# PAGE 2 : Créanciers & Fournisseurs
# ========================
elif page == "Créanciers & Fournisseurs":
    st.title("Suivi des Créanciers & Fournisseurs")

    # Données des créanciers et fournisseurs
    df_creanciers = pd.DataFrame({
        "Créancier": ["Banque A", "Banque B", "Banque C"],
        "Montant Total (€)": [20000, 15000, 12000],
        "Montant Réglé (€)": [12000, 7000, 5000],
        "Montant Restant (€)": [8000, 8000, 7000]
    })

    df_fournisseurs = pd.DataFrame({
        "Fournisseur": ["Fournisseur X", "Fournisseur Y", "Fournisseur Z"],
        "Montant Total (€)": [18000, 22000, 25000],
        "Montant Réglé (€)": [14000, 18000, 20000],
        "Montant Restant (€)": [4000, 4000, 5000]
    })

    # Affichage des tableaux
    st.write("### Créanciers")
    st.dataframe(df_creanciers)

    st.write("### Fournisseurs")
    st.dataframe(df_fournisseurs)

    # Évolution des paiements depuis Octobre
    date_range = pd.date_range(start="2024-10-01", periods=6, freq='M')
    df_evolution = pd.DataFrame({
        "Date": date_range,
        "Paiements Créanciers (€)": [10000, 9500, 9000, 8500, 8000, 7500],
        "Paiements Fournisseurs (€)": [8000, 7800, 7500, 7300, 7000, 6800]
    })

    # Graphique des paiements aux créanciers
    st.subheader("Évolution des paiements aux Créanciers")
    fig1 = px.line(df_evolution, x="Date", y="Paiements Créanciers (€)", markers=True, title="Paiements aux Créanciers")
    st.plotly_chart(fig1)

    # Graphique des paiements aux fournisseurs
    st.subheader("Évolution des paiements aux Fournisseurs")
    fig2 = px.line(df_evolution, x="Date", y="Paiements Fournisseurs (€)", markers=True, title="Paiements aux Fournisseurs")
    st.plotly_chart(fig2)

# ========================
# PAGE 3 : Solutions
# ========================
elif page == "Solutions":
    st.title("Solutions pour améliorer l'activité")

    # Recommandations pour le client
    st.write("### Recommandations pour le client XXXX")
    st.write("Statut : En redressement judiciaire")
    st.write("Activité : Commerce de détail")

    st.write("### Suggestions d'amélioration")
    suggestions = [
        "Optimiser la gestion de la trésorerie et négocier des délais de paiement plus longs.",
        "Renégocier les contrats avec les fournisseurs et rechercher des partenaires stratégiques.",
        "Développer une stratégie marketing adaptée, incluant la vente en ligne.",
        "Mettre en place des outils de suivi et de prévision pour anticiper les difficultés financières.",
        "Analyser la structure des coûts et réduire les dépenses non essentielles.",
        "Diversifier les sources de revenus en proposant de nouveaux services ou produits."
    ]
    for suggestion in suggestions:
        st.write(f"- {suggestion}")

