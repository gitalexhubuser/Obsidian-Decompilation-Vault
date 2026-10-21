---
offset: "0x004e5000"
module: "WoW/Source"
file: "WoW/Source/Glue/PatchDownloadGlue.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004e5000 — `CGlueMgr_PatchDownloadDeleteCommand`

- **Адрес (Offset):** `0x004e5000`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Glue/PatchDownloadGlue.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004e5000
bool CGlueMgr::PatchDownloadDeleteCommand(const char* path) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004e5000 в IDA Pro / Ghidra
