---
offset: "0x00805b10"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00805b10 — `Spell_C_SetCooldownLeft`

- **Адрес (Offset):** `0x00805b10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00805b10
void Spell_C_SetCooldownLeft(int32_t spellId, uint32_t itemId, uint32_t category, int32_t cooldownLeft, int32_t categoryCooldownLeft, bool onHold, int32_t pet) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00805b10 в IDA Pro / Ghidra
