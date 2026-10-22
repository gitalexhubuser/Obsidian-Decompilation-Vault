---
offset: "0x00421950"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/SFile2-Core.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00421950 — `SFile_OpenArchive`

### Описание
**SFile_OpenArchive** – функция библиотеки **StormLib**, отвечающая за открытие MPQ‑архивов (файловых контейнеров, используемых клиентом World of Warcraft).

**Зачем нужна:**
- Позволяет получить дескриптор архива, через который читаются файлы‑ресурсы (текстуры, модели, скрипты, данные UI).
- Необходима почти в любом модуле, работающем с клиентскими данными: загрузка UI‑файлов, чтение скриптов из `interface/*.lua`, обращение к игровому контенту (`Data/*.dbc`).

**Кто её использует:**
- Движки UI (FrameXML), скриптовый движок (Lua‑встроенный), модификации (AddOns), инструменты восстановления MPQ‑файлов.

**Аргументы:**
| Параметр | Тип | Описание |
|----------|-----|----------|
| `szArchiveName` | `LPCSTR` | Путь к MPQ‑файлу (можно указать относительный путь от корня клиентской папки). |
| `dwPriority` | `DWORD` | Приоритет загрузки (обычно `0`). |
| `dwFlags` | `DWORD` | Флаги открытия: `SFILE_OPEN_READONLY`, `SFILE_OPEN_DISK`, `SFILE_OPEN_LOCALIZED`. |
| `phArchive` | `HANDLE*` | Указатель, куда будет записан полученный дескриптор архива. |

**Пример использования в C++:**
```cpp
HANDLE hMpq = nullptr;
if (SFile_OpenArchive("Data\\Patch\\wow-update.MPQ", 0, SFILE_OPEN_READONLY, &hMpq))
{
    // Теперь можно работать с файлами внутри архива
    // …
    SFile_CloseArchive(hMpq);
}
else
{
    printf("Failed to open MPQ: error %lu\n", GetLastError());
}
```

**Типичные ошибки:**
- Неправильный путь → `GetLastError() == ERROR_FILE_NOT_FOUND`.
- Попытка открыть уже открытый архив без флага `SFILE_OPEN_ALLOWWRITE` → `ERROR_ACCESS_DENIED`.


- **Адрес (Offset):** `0x00421950`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/SFile2-Core.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00421950
int32_t STORMAPI SFile::OpenArchive(const char* path, int32_t priority, uint32_t flags, SArchive** archive) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00421950 в IDA Pro / Ghidra
