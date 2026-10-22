---
offset: "0x004218c0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/SFile2-Core.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004218c0 — `SFileGetFileSize`

### Описание
**SFileGetFileSize** возвращает размер конкретного файла внутри открытого MPQ‑архива.

**Зачем нужна:**
- Позволяет заранее выделить буфер нужного объёма перед чтением через `SFile_ReadFile`.
- Полезна при работе с большими бинарными ресурсами (модели, звуки), когда нужен точный размер.

**Кто её использует:**
- Модуль рендеринга (загрузка `.blp`‑текстур), аудио‑подсистема (загрузка `.wav`/`.mp3`), инструменты анализа.

**Аргументы:**
| Параметр | Тип | Описание |
|----------|-----|----------|
| `file` | `SFileImpl*` | Дескриптор файла (полученный через `SFileOpenFileEx`/`SFileOpenFile`). |
| `sizeHigh` | `uint32_t*` | Указатель на старшую 32‑битную часть 64‑битного размера (можно `nullptr`). |
| `sizeLow` | `uint32_t*` | Указатель, куда будет записана младшая часть размера.

**Пример использования:**
```cpp
HANDLE hFile = nullptr;
if (SFileOpenFileEx(hMpq, "Interface\\FrameXML\\UIParent.xml", SFILE_OPEN_READONLY, &hFile))
{
    DWORD low = 0, high = 0;
    if (SFile_GetFileSize(hFile, &high, &low))
    {
        uint64_t size = ((uint64_t)high << 32) | low;
        printf("File size = %llu bytes\n", size);
    }
    SFileCloseFile(hFile);
}
```

**Важно:** Если файл меньше 4 GB, старшую часть можно игнорировать (`nullptr`).


- **Адрес (Offset):** `0x004218c0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/SFile2-Core.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004218c0
uint32_t STORMAPI SFileGetFileSize(SFileImpl* file, uint32_t* sizeHigh) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004218c0 в IDA Pro / Ghidra
