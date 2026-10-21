---
offset: "0x0042c5c0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0042c5c0 — `ARCHIVEREC_SetBlockMd5`

- **Адрес (Offset):** `0x0042c5c0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0042c5c0
void System_SFile::ARCHIVEREC::SetBlockMd5(uint32_t index, const Blizzard::Util::Digest<16>& md5) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0042c5c0 в IDA Pro / Ghidra
