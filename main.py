import pandas as pd
import numpy as np

# Crear dataset de ejemplo
np.random.seed(42)
n_orders = 1000

df = pd.DataFrame({
    'order_id': range(1, n_orders + 1),
    'customer_id': np.random.randint(1, 201, n_orders),
    'product_id': np.random.randint(1, 51, n_orders),
    'quantity': np.random.randint(1, 5, n_orders),
    'unit_price': np.round(np.random.uniform(10, 500, n_orders), 2),
    'order_date': pd.date_range('2023-01-01', periods=n_orders, freq='H')[:n_orders],
    'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Cash'], n_orders),
    'customer_age': np.random.normal(35, 10, n_orders).clip(18, 80).astype(int),
    'shipping_region': np.random.choice(['North', 'South', 'East', 'West'], n_orders)
})

# Introducir valores faltantes
mask = np.random.random(n_orders) < 0.05
df.loc[mask, 'customer_age'] = np.nan

print("Dataset cargado exitosamente")

print(df.shape)
print(df.dtypes)
print(df.head())
print(df.tail())

## Análisis de calidad de datos

print(df.isnull().sum())
print((1 - df.isnull().sum() / len(df)) * 100)

for col in df.select_dtypes(include=['object']).columns:
    print(col, df[col].nunique())

print(df.select_dtypes(include=[np.number]).describe())

## Preguntas exploratorias iniciales

print(df['shipping_region'].value_counts())
print(df['payment_method'].value_counts().index[0])
print(df['order_date'].min(), df['order_date'].max())
print(df['customer_age'].mean())
