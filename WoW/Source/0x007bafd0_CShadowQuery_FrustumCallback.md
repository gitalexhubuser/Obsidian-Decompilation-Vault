---
offset: "0x007bafd0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/ShadowQuery.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007bafd0 — `CShadowQuery_FrustumCallback`

- **Адрес (Offset):** `0x007bafd0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/ShadowQuery.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007bafd0
void CShadowQuery::FrustumCallback(CFrustum& frustum, C44Matrix& matrix, const C3Vector& direction, CShadowCacheQueryData& data, int32_t band) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007bafd0 в IDA Pro / Ghidra
