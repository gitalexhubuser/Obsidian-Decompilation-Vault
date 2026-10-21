---
offset: "0x004e5420"
module: "WoW/Source"
file: "WoW/Source/Glue/PatchDownloadGlue.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004e5420 — `CGlueMgr_PatchFailed`

- **Адрес (Offset):** `0x004e5420`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Glue/PatchDownloadGlue.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004e5420
void CGlueMgr::PatchFailed(int32_t reason, uint32_t data) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004e5420 в IDA Pro / Ghidra
