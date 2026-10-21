---
offset: "0x004e51e0"
module: "WoW/Source"
file: "WoW/Source/Glue/PatchDownloadGlue.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004e51e0 — `CGlueMgr_GetPatchFolder`

- **Адрес (Offset):** `0x004e51e0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Glue/PatchDownloadGlue.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004e51e0
size_t CGlueMgr::GetPatchFolder(char* buffer, uint32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004e51e0 в IDA Pro / Ghidra
