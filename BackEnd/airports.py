import database
def airport1():
    sql_airport1 = (f"""SELECT airport.name as 'airport name', country.name as 'country name', latitude_deg, longitude_deg, ident FROM airport 
    INNER JOIN country ON airport.iso_country=country.iso_country
    WHERE airport.name like "%Svalbard%";""")
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(sql_airport1)
    start = cursor.fetchone()
    return start

#Seuraavasta Venäjä pois lähinnä koska se on sekä EU että AS
def airport2(item):
    sql_airport2 = (f"""SELECT airport.name as 'airport name', country.name as 'country name', latitude_deg, longitude_deg, ident FROM airport 
    INNER JOIN country ON airport.iso_country=country.iso_country 
    WHERE airport.continent='{item}' and type='large_airport' and country.name!='Russia'
    GROUP BY country.name ORDER BY RAND() LIMIT 7;""")
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(sql_airport2)
    result = cursor.fetchall()
    return result
def airport3():
    sql_airport3 = (f"""SELECT airport.name as 'airport name', country.name as 'country name', latitude_deg, longitude_deg, ident FROM airport 
    INNER JOIN country ON airport.iso_country=country.iso_country 
    WHERE airport.continent='AN' and type='medium_airport' 
    ORDER BY RAND() LIMIT 1;""")
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(sql_airport3)
    end = cursor.fetchone()
    return end

print(airport1())
print(airport2('AS'))
print(airport3())