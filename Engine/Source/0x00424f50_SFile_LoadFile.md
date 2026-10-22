---
offset: "0x00424f50"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/SFile2-Core.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00424f50 — `SFile_LoadFile`

### Описание
**SFile_LoadFile** – функция‑оболочка StormLib, загружающая весь файл из MPQ‑архива в память одним вызовом.

**Зачем нужна:**
- Упрощает чтение небольших файлов (скриптов, конфигураций, DBC‑таблиц).
- Автоматически управляет буфером: выделяет нужный объём и возвращает указатель + размер.

**Кто её использует:**
- UI‑модуль (загрузка `Interface/*.xml`), скриптовый движок (загрузка `*.lua`), инструменты анализа (парсинг `*.dbc`).

**Аргументы:**
| Параметр | Тип | Описание |
|----------|-----|----------|
| `hArchive` | `HANDLE` | Дескриптор MPQ‑архива (от `SFile_OpenArchive`). |
| `szFileName` | `LPCSTR` | Путь к файлу внутри архива, например `"Interface\\FrameXML\\UIParent.xml"`. |
| `lpBuffer` | `void**` | Указатель‑на‑указатель, в который будет записан буфер с данными. |
| `pdwFileSize` | `DWORD*` | Указатель, куда будет записан размер загруженного файла (в байтах). |
| `dwFlags` | `DWORD` | Флаги (обычно `0`). |

**Пример использования:**
```cpp
void* pData = nullptr;
DWORD dwSize = 0;
if (SFile_LoadFile(hMpq, "Interface\\FrameXML\\UIParent.xml", &pData, &dwSize, 0))
{
    // pData содержит содержимое файла, размер – dwSize
    // Обрабатываем XML…
    SFile_FreeFile(pData);   // Освобождаем буфер
}
else
{
    printf("Load failed: %lu\n", GetLastError());
}
```

**Важно:** После завершения работы обязательно вызвать `SFile_FreeFile` – иначе произойдёт утечка памяти.


- **Адрес (Offset):** `0x00424f50`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/SFile2-Core.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00424f50
int32_t STORMAPI SFile::LoadFile(const char* name, void** data, uint32_t* size, uint32_t extra, SOVERLAPPED* overlapped) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00424f50 в IDA Pro / Ghidra
