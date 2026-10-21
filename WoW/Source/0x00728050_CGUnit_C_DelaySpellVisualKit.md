---
offset: "0x00728050"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Unit_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00728050 — `CGUnit_C_DelaySpellVisualKit`

- **Адрес (Offset):** `0x00728050`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Unit_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00728050
DelayedSpellVisualKit* CGUnit_C::DelaySpellVisualKit(int32_t spellId, int32_t kitId, int32_t kitType, const C3Vector* position, WOWGUID targetGuid, int32_t a7, int32_t a8, int32_t delay, int32_t a10, int32_t a11) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00728050 в IDA Pro / Ghidra
