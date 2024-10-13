
# Hand Generator

### Описание проекта

**Hand Generator** — это приложение для генерации реалистичных 3D-моделей человеческих ладоней. Этот инструмент позволяет пользователям создавать высокоразрешенные и детализированные изображения ладоней с различными характеристиками. Основной движок приложения использует продвинутые нейронные сети, такие как **ProGAN** (Progressive GAN), для генерации изображений высокого качества. **ProGAN** является одной из самых эффективных технологий для создания реалистичных изображений в области генерации 3D-моделей и порцеланного тела.

---

## Установка

### Шаг 1: Клонирование репозитория

Для начала клонируйте репозиторий с GitHub на ваше устройство:

```bash
git clone https://github.com/NAKAZUKA/hand-generator.git
cd hand-generator
```

### Шаг 2: Установка виртуального окружения

#### Windows:
```bash
python -m venv venv
venv\Scriptsctivate
```

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Шаг 3: Установка зависимостей

После активации виртуального окружения установите все необходимые зависимости:

```bash
pip install -r requirements.txt
```

---

## Запуск приложения

Чтобы запустить генератор ладоней, выполните следующие шаги:

1. Запустите файл **Start.py**:
   ```bash
   python Start.py
   ```

2. После запуска, заполните все необходимые параметры и нажмите кнопку **SET Selected Options**.

3. Закройте приложение, нажав на крестик. После завершения работы в папке **Output** будут сохранены сгенерированные изображения.
