---
offset: "0x00440b10"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/RepairCache.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00440b10 — `RepairCache_AddEntry`

- **Адрес (Offset):** `0x00440b10`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/RepairCache.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00440b10
bool Blizzard::Repair::RepairCache::AddEntry(const Blizzard::Util::Digest<16>& md5, int64_t index, uint32_t offset, uint32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00440b10 в IDA Pro / Ghidra
