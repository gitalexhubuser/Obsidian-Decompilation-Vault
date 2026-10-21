---
offset: "0x006321b0"
module: "WoW/Source"
file: "WoW/Source/Net/NetClient/NetClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006321b0 — `ComputeProofOfWork`

- **Адрес (Offset):** `0x006321b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Net/NetClient/NetClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006321b0
static bool __stdcall ComputeProofOfWork(const SHA1_CONTEXT* context, uint32_t difficulty, uint64_t* proof) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006321b0 в IDA Pro / Ghidra
