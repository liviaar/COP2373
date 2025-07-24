# This program creates a database to track population changes for 10 Florida
# cities from 2023 to 2043, simulates annual growth or decline, and displays a
# graph of a city's population over time. - Livia Augusto Razera, Assignment 13

import sqlite3
import random
import matplotlib.pyplot as plt


# Function that creates a database and initial population table
def create_population_database():
    conn = sqlite3.connect("population_LR.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    cities = {
        "Miami": 450000,
        "Orlando": 310000,
        "Tampa": 395000,
        "Jacksonville": 950000,
        "Tallahassee": 200000,
        "St. Petersburg": 260000,
        "Hialeah": 230000,
        "Fort Lauderdale": 180000,
        "Cape Coral": 220000,
        "Gainesville": 140000
    }
    for city, population in cities.items():
        cur.execute("INSERT INTO population VALUES (?, ?, ?)",
                    (city, 2023, population))
    conn.commit()
    conn.close()


# Function that simulates 20 years of population changes and insert into
# database
def simulate_population_change():
    conn = sqlite3.connect("population_LR.db")
    cur = conn.cursor()
    cur.execute("SELECT city, population FROM population WHERE year = 2023")
    initial_data = cur.fetchall()

    for city, pop in initial_data:
        current_population = pop
        for year in range(2024, 2044):
            rate = random.uniform(-0.01, 0.03)  # Growth between -1% and +3%
            current_population = int(current_population * (1 + rate))
            cur.execute("INSERT INTO population VALUES (?, ?, ?)",
                        (city, year, current_population))

    conn.commit()
    conn.close()


# Function that asks user to choose a city and plot population growth
def plot_city_population():
    cities = [
        "Miami", "Orlando", "Tampa", "Jacksonville", "Tallahassee",
        "St. Petersburg", "Hialeah", "Fort Lauderdale", "Cape Coral",
        "Gainesville"
    ]
    print("\nChoose a city to view population growth:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    choice = int(input("Enter the number of the city: "))
    selected_city = cities[choice - 1]

    conn = sqlite3.connect("population_LR.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT year, population FROM population WHERE city = ? ORDER BY year",
        (selected_city,))
    data = cur.fetchall()
    conn.close()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.figure(figsize=(10, 6))
    plt.plot(years, populations, marker='o')
    plt.title(f"Population Growth for {selected_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Call out the functions.
create_population_database()
simulate_population_change()
plot_city_population()