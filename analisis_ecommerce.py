import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# ================================================
# 1. CREAR DATASET DE ECOMMERCE
# ================================================

data = {
    'id_orden': range(1, 51),
    'fecha': [
        '2026-01-05','2026-01-12','2026-01-18','2026-01-25','2026-01-30',
        '2026-02-03','2026-02-08','2026-02-14','2026-02-20','2026-02-25',
        '2026-03-02','2026-03-07','2026-03-11','2026-03-15','2026-03-20',
        '2026-03-25','2026-03-28','2026-04-02','2026-04-06','2026-04-10',
        '2026-04-14','2026-04-18','2026-04-22','2026-04-26','2026-04-30',
        '2026-05-02','2026-05-05','2026-05-08','2026-05-10','2026-05-12',
        '2026-01-08','2026-01-22','2026-02-05','2026-02-18','2026-03-04',
        '2026-03-18','2026-04-01','2026-04-15','2026-05-01','2026-05-06',
        '2026-01-15','2026-02-10','2026-03-08','2026-04-05','2026-05-03',
        '2026-01-20','2026-02-22','2026-03-22','2026-04-20','2026-05-09'
    ],
    'categoria': [
        'Electrónica','Ropa','Electrónica','Hogar','Ropa',
        'Electrónica','Hogar','Ropa','Electrónica','Hogar',
        'Ropa','Electrónica','Hogar','Ropa','Electrónica',
        'Hogar','Ropa','Electrónica','Hogar','Ropa',
        'Electrónica','Hogar','Ropa','Electrónica','Hogar',
        'Ropa','Electrónica','Hogar','Ropa','Electrónica',
        'Hogar','Ropa','Electrónica','Hogar','Ropa',
        'Electrónica','Hogar','Ropa','Electrónica','Hogar',
        'Ropa','Electrónica','Hogar','Ropa','Electrónica',
        'Hogar','Ropa','Electrónica','Hogar','Ropa'
    ],
    'producto': [
        'Notebook','Remera','Auriculares','Silla','Pantalón',
        'Tablet','Lámpara','Zapatillas','Monitor','Escritorio',
        'Campera','Smartphone','Almohadón','Vestido','Teclado',
        'Estante','Buzo','Mouse','Cuadro','Falda',
        'Notebook','Silla','Remera','Auriculares','Lámpara',
        'Pantalón','Tablet','Escritorio','Zapatillas','Monitor',
        'Almohadón','Campera','Smartphone','Estante','Vestido',
        'Teclado','Cuadro','Buzo','Mouse','Falda',
        'Remera','Notebook','Silla','Auriculares','Lámpara',
        'Pantalón','Tablet','Escritorio','Zapatillas','Monitor'
    ],
    'cantidad': [1,2,1,1,3,1,2,1,1,1,2,1,3,1,1,2,1,1,2,2,1,1,3,1,2,2,1,1,1,1,3,2,1,2,1,1,2,1,1,3,2,1,1,1,2,3,1,1,2,1],
    'precio_unitario': [
        85000,5500,12000,45000,8000,
        55000,3500,18000,75000,38000,
        15000,120000,2500,12000,9500,
        22000,8500,4500,6000,7000,
        85000,45000,5500,12000,3500,
        8000,55000,38000,18000,75000,
        2500,15000,120000,22000,12000,
        9500,6000,8500,4500,7000,
        5500,85000,45000,12000,3500,
        8000,55000,38000,18000,75000
    ],
    'pais': [
        'Argentina','Argentina','España','Argentina','España',
        'Argentina','España','Argentina','España','Argentina',
        'Argentina','España','Argentina','España','Argentina',
        'España','Argentina','Argentina','España','Argentina',
        'España','Argentina','Argentina','España','Argentina',
        'España','Argentina','España','Argentina','Argentina',
        'España','Argentina','Argentina','España','Argentina',
        'España','Argentina','Argentina','España','Argentina',
        'España','Argentina','Argentina','España','Argentina',
        'España','Argentina','Argentina','España','Argentina'
    ]
}

df = pd.DataFrame(data)
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month
df['nombre_mes'] = df['fecha'].dt.strftime('%B')
df['total'] = df['cantidad'] * df['precio_unitario']

# ================================================
# 2. ANÁLISIS
# ================================================

print("=== RESUMEN GENERAL ===")
print(f"Total órdenes:     {len(df)}")
print(f"Total ingresos:    ${df['total'].sum():,.0f}")
print(f"Ticket promedio:   ${df['total'].mean():,.0f}")
print(f"Países:            {df['pais'].nunique()}")

print("\n=== VENTAS POR CATEGORÍA ===")
print(df.groupby('categoria')['total'].sum().sort_values(ascending=False))

print("\n=== TOP 5 PRODUCTOS ===")
print(df.groupby('producto')['total'].sum().sort_values(ascending=False).head(5))

print("\n=== VENTAS POR MES ===")
print(df.groupby('mes')['total'].sum().sort_values())

# ================================================
# 3. GRÁFICOS
# ================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Análisis de Ventas Ecommerce - 2026', fontsize=16, fontweight='bold')

# Gráfico 1: Ventas por categoría
ventas_cat = df.groupby('categoria')['total'].sum().sort_values(ascending=True)
axes[0,0].barh(ventas_cat.index, ventas_cat.values, color='steelblue')
axes[0,0].set_title('Ingresos por Categoría')
axes[0,0].set_xlabel('Total ($)')

# Gráfico 2: Evolución mensual
ventas_mes = df.groupby('mes')['total'].sum()
axes[0,1].plot(ventas_mes.index, ventas_mes.values, marker='o', color='green', linewidth=2)
axes[0,1].set_title('Evolución Mensual de Ventas')
axes[0,1].set_xlabel('Mes')
axes[0,1].set_ylabel('Total ($)')

# Gráfico 3: Ventas por país
ventas_pais = df.groupby('pais')['total'].sum()
axes[1,0].pie(ventas_pais.values, labels=ventas_pais.index, autopct='%1.1f%%', colors=['steelblue','orange'])
axes[1,0].set_title('Distribución por País')

# Gráfico 4: Top 5 productos
top5 = df.groupby('producto')['total'].sum().sort_values(ascending=False).head(5)
axes[1,1].bar(top5.index, top5.values, color='coral')
axes[1,1].set_title('Top 5 Productos')
axes[1,1].set_xlabel('Producto')
axes[1,1].set_ylabel('Total ($)')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('dashboard_ecommerce.png', dpi=150, bbox_inches='tight')
plt.show()

print("\nGráfico guardado: dashboard_ecommerce.png")