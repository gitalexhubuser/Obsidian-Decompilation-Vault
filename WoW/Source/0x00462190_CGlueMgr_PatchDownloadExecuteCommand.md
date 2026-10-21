---
offset: "0x00462190"
module: "WoW/Source"
file: "WoW/Source/Glue/Win64/PatchDownloadGlue.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00462190 — `CGlueMgr_PatchDownloadExecuteCommand`

- **Адрес (Offset):** `0x00462190`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Glue/Win64/PatchDownloadGlue.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00462190
bool CGlueMgr::PatchDownloadExecuteCommand(const char* path, const char* arguments) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00462190 в IDA Pro / Ghidra
