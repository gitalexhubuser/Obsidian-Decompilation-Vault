---
offset: "0x004e59c0"
module: "WoW/Source"
file: "WoW/Source/Glue/ScanDLLGlue.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004e59c0 — `DownloadDllCallback`

- **Адрес (Offset):** `0x004e59c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Glue/ScanDLLGlue.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004e59c0
static bool DownloadDllCallback(void* param, const char* data, uint32_t size, bool done, HTTPError::ErrorCode error) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004e59c0 в IDA Pro / Ghidra
