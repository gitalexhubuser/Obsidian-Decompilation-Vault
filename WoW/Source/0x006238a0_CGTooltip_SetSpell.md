---
offset: "0x006238a0"
module: "WoW/Source"
file: "WoW/Source/UIUtil/Tooltip.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006238a0 — `CGTooltip_SetSpell`

- **Адрес (Offset):** `0x006238a0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/UIUtil/Tooltip.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006238a0
int32_t CGTooltip::SetSpell(int32_t spellId, int32_t brief, uint32_t cooldown, int32_t isPet, int32_t showRank, int32_t isInspect, int32_t a8, const TalentRec* talent, CGTalentGroup_C* talentGroup, int32_t append, int32_t usePreview, int32_t a13, int32_t rank, int32_t maxRank, int32_t showLearn) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006238a0 в IDA Pro / Ghidra
