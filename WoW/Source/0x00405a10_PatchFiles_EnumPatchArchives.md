---
offset: "0x00405a10"
module: "WoW/Source"
file: "WoW/Source/WowServices/PatchFiles.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00405a10 — `PatchFiles_EnumPatchArchives`

- **Адрес (Offset):** `0x00405a10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/PatchFiles.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00405a10
int32_t PatchFiles::EnumPatchArchives(OS_FILE_DATA& data, void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00405a10 в IDA Pro / Ghidra
