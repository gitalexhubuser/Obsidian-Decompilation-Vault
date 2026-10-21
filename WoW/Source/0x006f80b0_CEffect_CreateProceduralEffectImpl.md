---
offset: "0x006f80b0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Effect_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006f80b0 — `CEffect_CreateProceduralEffectImpl`

- **Адрес (Offset):** `0x006f80b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Effect_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006f80b0
void CEffect::CreateProceduralEffectImpl(int32_t expireTime, float param, uint32_t spellId, const SpellVisualKitRec* kit, const WOWGUID* guid, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006f80b0 в IDA Pro / Ghidra
