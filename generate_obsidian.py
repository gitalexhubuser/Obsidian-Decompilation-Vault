import os
import re

# Определяем базовую директорию проекта (папка, где лежит сам скрипт)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Папка, куда сохранятся карточки Obsidian
VAULT_DIR = os.path.join(BASE_DIR, "Obsidian_Vault")

def clean_filename(name):
    """Убирает недопустимые символы из имени файла"""
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def get_signature(lines, start_idx):
    """Ищет первую непустую строку C++ кода после комментария OFFSET"""
    idx = start_idx + 1
    sig_lines = []
    while idx < len(lines):
        line = lines[idx].strip()
        if not line or line.startswith("//") or line.startswith("/*"):
            idx += 1
            continue
        sig_lines.append(line)
        if line.endswith("{") or line.endswith(";") or line.endswith(")") or "{" in line:
            break
        idx += 1
        if len(sig_lines) >= 3:
            break
    return " ".join(sig_lines) if sig_lines else "Unknown_Function"

print(f"Сканируем директорию: {BASE_DIR}")
print(f"Целевая папка Obsidian: {VAULT_DIR}")
print("Начинаем генерацию карточек Obsidian...")

found_count = 0
scanned_files = 0

for root, _, files in os.walk(BASE_DIR):
    # Исключаем папку самого хранилища Obsidian, .git и build-директории
    if "Obsidian_Vault" in root or ".git" in root or ".vs" in root:
        continue
        
    for file in files:
        if file.lower().endswith((".cpp", ".h", ".hpp")):
            scanned_files += 1
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, BASE_DIR).replace("\\", "/")
            
            # Определяем модуль на основе относительного пути
            parts = rel_path.split("/")
            module_name = "General"
            for idx, part in enumerate(parts):
                if part.lower() in ["engine", "wow"] and idx + 1 < len(parts):
                    module_name = f"{part}/{parts[idx+1]}"
                    break
            
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                
                for i, line in enumerate(lines):
                    # Поиск метки OFFSET без строгого учета пробелов и регистра
                    match = re.search(r"//\s*OFFSET:\s*(0x[0-9a-fA-F]+)", line, re.IGNORECASE)
                    if match:
                        offset_str = match.group(1).lower()
                        func_sig = get_signature(lines, i)
                        
                        func_name = "Function"
                        name_match = re.search(r"(\b\w+::\b\w+|\b\w+)\s*\(", func_sig)
                        if name_match:
                            func_name = name_match.group(1).replace("::", "_")
                        
                        target_dir = os.path.join(VAULT_DIR, module_name)
                        os.makedirs(target_dir, exist_ok=True)
                        
                        card_filename = f"{offset_str}_{clean_filename(func_name)}.md"
                        card_path = os.path.join(target_dir, card_filename)
                        
                        clean_mod = clean_filename(module_name.lower().replace('/', '_'))
                        md_content = f"""---
offset: "{offset_str}"
module: "{module_name}"
file: "{rel_path}"
tags:
  - wowdecomp
  - offset
  - module/{clean_mod}
---

# {offset_str} — `{func_name}`

- **Адрес (Offset):** `{offset_str}`
- **Модуль:** `{module_name}`
- **Файл исходника:** `{rel_path}`

## Сигнатура C++
```cpp
// OFFSET: {offset_str}
{func_sig}
```

## Исследование и заметки
- [ ] Открыть адрес {offset_str} в IDA Pro / Ghidra
"""
                        with open(card_path, "w", encoding="utf-8") as card_file:
                            card_file.write(md_content)
                        found_count += 1
            except Exception as e:
                print(f"Ошибка при обработке {file_path}: {e}")

print(f"\nПроверено файлов исходников: {scanned_files}")
print(f"Готово! Успешно создано {found_count} карточек в папке '{VAULT_DIR}'.")
print("Теперь вы можете открыть папку 'Obsidian_Vault' как новое хранилище (Vault) в Obsidian.")