# TuxAldo

> Aplicación móvil de gestión de finanzas personales — software libre, local y sin restricciones.  
> Personal finance mobile app — free software, local storage, no restrictions.

---

## 🇪🇸 Español

### ¿Qué es TuxAldo?

TuxAldo es una aplicación móvil de gestión de finanzas personales desarrollada íntegramente con herramientas de software libre. Permite registrar ingresos y egresos diarios, y visualizar el balance financiero de forma clara en cuatro niveles: diario, semanal, mensual y anual.

El proyecto nace de la convicción de que el control sobre las finanzas personales es un derecho, y que las herramientas para ejercerlo deben ser accesibles para todos — sin registro en servidores externos, sin muros de pago y sin explotación de datos.

### Tecnologías

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3 |
| Interfaz | Flet (Flutter/Dart bajo Python) |
| Base de datos | SQLite3 |
| Plataforma objetivo | Android |
| Licencia | AGPL-3.0 |

### Funcionalidades

- Registro de transacciones diarias con título, valor, categoría y descripción
- Cálculo automático de balance (positivo o negativo) por día, semana, mes y año
- Navegación jerárquica: Año → Mes → Semana → Día → Transacciones
- Almacenamiento local — sin internet, sin servidores externos
- Interfaz simple e intuitiva para el público general

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/AlexEscB/TuxAldo.git
cd TuxAldo

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install flet

# Ejecutar en escritorio
cd TuxAldo/src
flet run
```

### Compilar APK

```bash
flet build apk
```

> Requiere Flutter SDK y Android SDK. Flet los descarga automáticamente en el primer build.

### Estructura del proyecto

```
TuxAldo/src/
├── main.py                          # Punto de entrada
├── config.py                        # Configuración global (ruta DB)
├── controllers/                     # Lógica de negocio
│   ├── home_controller.py
│   ├── period_controller.py
│   ├── add_transaction_controller.py
│   └── controller_create_mwd.py
├── Database/
│   ├── database_connector.py        # Creación de tablas
│   └── Repositories/                # DAOs — acceso a datos
├── UI/
│   ├── views/                       # Pantallas principales
│   └── Components/                  # Componentes reutilizables
└── utils/
    └── date_utils.py                # Utilidades de fecha en español
```

### Licencia

Distribuido bajo la licencia [AGPL-3.0](https://github.com/AlexEscB/TuxAldo?tab=AGPL-3.0-1-ov-file). Cualquier persona puede usar, estudiar, modificar y redistribuir este software, incluso cuando se utilice como servicio en red.

### Autor

Alejandro Escobar Barrios — Universidad Distrital Francisco José de Caldas

---

## 🇬🇧 English

### What is TuxAldo?

TuxAldo is a personal finance mobile app built entirely with free and open source software. It lets you record daily income and expenses, and clearly visualize your financial balance across four levels: daily, weekly, monthly, and yearly.

The project is built on the belief that personal financial control is a right — and that the tools to exercise it should be accessible to everyone, without external server registration, paywalls, or data exploitation.

### Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3 |
| UI Framework | Flet (Flutter/Dart via Python) |
| Database | SQLite3 |
| Target Platform | Android |
| License | AGPL-3.0 |

### Features

- Daily transaction recording with title, amount, category, and description
- Automatic balance calculation (positive or negative) per day, week, month, and year
- Hierarchical navigation: Year → Month → Week → Day → Transactions
- Local storage — no internet required, no external servers
- Simple and intuitive interface for general audiences

### Installation

```bash
# Clone the repository
git clone https://github.com/AlexEscB/TuxAldo.git
cd TuxAldo

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install flet

# Run on desktop
cd TuxAldo/src
flet run
```

### Build APK

```bash
flet build apk
```

> Requires Flutter SDK and Android SDK. Flet downloads them automatically on the first build.

### Project Structure

```
TuxAldo/src/
├── main.py                          # Entry point
├── config.py                        # Global config (DB path)
├── controllers/                     # Business logic
│   ├── home_controller.py
│   ├── period_controller.py
│   ├── add_transaction_controller.py
│   └── controller_create_mwd.py
├── Database/
│   ├── database_connector.py        # Table creation
│   └── Repositories/                # DAOs — data access
├── UI/
│   ├── views/                       # Main screens
│   └── Components/                  # Reusable components
└── utils/
    └── date_utils.py                # Spanish date utilities
```

### License

Distributed under the [AGPL-3.0 license](https://github.com/AlexEscB/TuxAldo?tab=AGPL-3.0-1-ov-file). Anyone can use, study, modify, and redistribute this software, even when used as a network service.

### Author

Alejandro Escobar Barrios — Universidad Distrital Francisco José de Caldas
