---
offset: "0x0086d1d0"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsIME.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086d1d0 — `OsIMEGetCandidates`

- **Адрес (Offset):** `0x0086d1d0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsIME.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086d1d0
int32_t OsIMEGetCandidates(uint32_t listMask, uint32_t& pageStart, uint32_t& pageSize, uint32_t& count, uint32_t& selection, TSGrowableArray<OsIMECandidate>& candidates) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086d1d0 в IDA Pro / Ghidra
