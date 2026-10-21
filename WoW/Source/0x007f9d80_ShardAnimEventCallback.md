---
offset: "0x007f9d80"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/SpellVisuals.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007f9d80 — `ShardAnimEventCallback`

- **Адрес (Offset):** `0x007f9d80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/SpellVisuals.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007f9d80
static void ShardAnimEventCallback(CM2Model* model, uint32_t boneId, uint32_t eventId, uint32_t data, const C3Vector* position, uint32_t time, uint64_t param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007f9d80 в IDA Pro / Ghidra
