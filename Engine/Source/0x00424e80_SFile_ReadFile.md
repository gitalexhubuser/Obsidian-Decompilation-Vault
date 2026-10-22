---
offset: "0x00424e80"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/SFile2-Core.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00424e80 — `SFile_ReadFile`

### Описание
**SFile_ReadFile** – базовая функция чтения произвольного блока данных из уже открытого файла MPQ‑архива.

**Зачем нужна:**
- Позволяет считывать файлы частично (по частям), что удобно для потоковой загрузки больших ресурсов (модели, аудио).
- Поддерживает перемещение указателя через `SFileSetFilePointer` и чтение в заранее выделенный буфер.

**Кто её использует:**
- Рендерер (построчное чтение `.blp`‑текстур), аудио‑модуль (чтение звуковых файлов), скриптовый движок (чтение Lua‑байтов).

**Аргументы:**
| Параметр | Тип | Описание |
|----------|-----|----------|
| `archive` | `SArchive*` | Дескриптор открытого MPQ‑архива. |
| `name` | `const char*` | Путь к файлу внутри архива. |
| `data` | `void**` | Указатель‑на‑указатель, куда будет записан буфер с данными. |
| `size` | `uint32_t*` | Указатель, куда будет записан размер реально прочитанных байт. |
| `extra` | `uint32_t` | Дополнительные флаги (обычно 0). |
| `flags` | `uint32_t` | Флаги чтения (обычно 0). |
| `overlapped` | `SOVERLAPPED*` | Структура для асинхронного чтения (можно `nullptr`). |

**Пример использования:**
```cpp
HANDLE hFile = nullptr;
if (SFileOpenFileEx(hMpq, "Interface\\FrameXML\\UIParent.xml", SFILE_OPEN_READONLY, &hFile))
{
    const DWORD chunk = 4096;
    BYTE buffer[chunk];
    DWORD read = 0;
    while (SFile_ReadFile(hFile, buffer, chunk, &read, 0) && read > 0)
    {
        // Обрабатываем полученные данные…
    }
    SFileCloseFile(hFile);
}
```

**Важно:** Если файл небольшой, предпочтительнее использовать `SFile_LoadFile`, которое автоматически выделит буфер и вернёт его целиком.


- **Адрес (Offset):** `0x00424e80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/SFile2-Core.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00424e80
int32_t STORMAPI SFile::ReadFile(SArchive* archive, const char* name, void** data, uint32_t* size, uint32_t extra, uint32_t flags, SOVERLAPPED* overlapped) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00424e80 в IDA Pro / Ghidra
