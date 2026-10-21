---
offset: "0x00558200"
module: "WoW/Source"
file: "WoW/Source/Ui/LFGListParty.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00558200 — `LFGListPlayer_LFGListPlayer`

- **Адрес (Offset):** `0x00558200`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/LFGListParty.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00558200
LFGListPlayer::LFGListPlayer(const LFGListPlayer& source) : m_index(source.m_index), m_partyIndex(source.m_partyIndex), m_party(source.m_party), m_level(source.m_level), m_class(source.m_class), m_race(source.m_race), m_armor(source.m_armor), m_spellDamage(source.m_spellDamage), m_spellHeal(source.m_spellHeal), m_critMelee(source.m_critMelee), m_critRanged(source.m_critRanged), m_critSpell(source.m_critSpell), m_mp5(source.m_mp5), m_mp5Combat(source.m_mp5Combat), m_attackPower(source.m_attackPower), m_agility(source.m_agility), m_maxHealth(source.m_maxHealth), m_maxMana(source.m_maxMana), unk_0064(source.unk_0064), m_avgItemLevel(source.m_avgItemLevel), m_defenseSkill(source.m_defenseSkill), m_dodge(source.m_dodge), m_block(source.m_block), m_parry(source.m_parry), m_haste(source.m_haste), m_expertise(source.m_expertise), m_areaID(source.m_areaID), unk_0088(source.unk_0088), m_leader(source.m_leader), m_roles(source.m_roles), unk_0198(source.unk_0198), m_encounterMask(source.m_encounterMask) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00558200 в IDA Pro / Ghidra
