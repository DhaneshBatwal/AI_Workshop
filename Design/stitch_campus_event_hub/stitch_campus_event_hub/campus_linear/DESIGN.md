---
name: Campus Linear
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#464555'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#777587'
  outline-variant: '#c7c4d8'
  surface-tint: '#4d44e3'
  primary: '#3525cd'
  on-primary: '#ffffff'
  primary-container: '#4f46e5'
  on-primary-container: '#dad7ff'
  inverse-primary: '#c3c0ff'
  secondary: '#712ae2'
  on-secondary: '#ffffff'
  secondary-container: '#8a4cfc'
  on-secondary-container: '#fffbff'
  tertiary: '#005338'
  on-tertiary: '#ffffff'
  tertiary-container: '#006e4c'
  on-tertiary-container: '#7df1bd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2dfff'
  primary-fixed-dim: '#c3c0ff'
  on-primary-fixed: '#0f0069'
  on-primary-fixed-variant: '#3323cc'
  secondary-fixed: '#eaddff'
  secondary-fixed-dim: '#d2bbff'
  on-secondary-fixed: '#25005a'
  on-secondary-fixed-variant: '#5a00c6'
  tertiary-fixed: '#85f8c4'
  tertiary-fixed-dim: '#68dba9'
  on-tertiary-fixed: '#002114'
  on-tertiary-fixed-variant: '#005137'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.025em
  headline-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: -0.006em
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0em
  label-md:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: -0.005em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0em
  mono-code:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: -0.01em
  mono-micro:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '400'
    lineHeight: 14px
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-desktop: 1.5rem
  margin: 1rem
  margin-tablet: 1.5rem
  margin-desktop: 2.5rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.875rem
  space-lg: 1.25rem
  space-xl: 2rem
---

## Brand & Style

This design system establishes an ultra-refined, productivity-first digital workspace for collegiate organizations, campus leaders, and student attendees. Drawing inspiration from modern engineering and knowledge-base tools like Linear and Notion, the experience prioritizes dense, scannable clarity, mechanical precision, and tactile satisfaction.

### Visual Style
- **Minimalist Precision & Tactile Utility:** Cool slate neutral foundations, 1px crisp architectural containment borders, and functional data density.
- **Translucent Depth:** Subtle layered backdrop blurs (`backdrop-blur-md`) on persistent headers, sidebars, context menus, and interactive popovers to provide structural context without clutter.
- **Accented Energy:** Deep indigo, energetic iris, and electric violet focal points signify primary action paths and active states, balanced with purposeful warm amber, coral, and emerald indicators for ticket statuses, capacity loads, and verification tags.
- **Target Audience:** Ambitious student club organizers, university department heads, and tech-forward students who demand the speed of keyboard shortcuts, dense information hierarchies, and frictionless RSVP workflows.

## Colors

The palette balances cool, slate-tinted canvas neutrals with high-chroma violet-indigo accents to evoke an academic yet deeply modern craft.

### Functional Palette Mapping
- **Canvas & Backgrounds:**
  - Base Application Canvas: `#F8FAFC` (Slate 50)
  - Card & Container Surface: `#FFFFFF` (Pure White)
  - Secondary/Sidebar Surface: `#F1F5F9` (Slate 100)
  - Hover & Pressed Surface: `#E2E8F0` (Slate 200)
- **Borders & Dividers:**
  - Default Structural Border: `#E2E8F0` (Slate 200)
  - Subtle Inset Divider: `#F1F5F9` (Slate 100)
  - Focus Ring & Active Border: `#4F46E5` (Indigo 600) with a 20% alpha outer glow ring.
- **Primary & Interactive Accents:**
  - Primary Base: `#4F46E5` (Indigo 600)
  - Primary Hover: `#4338CA` (Indigo 700)
  - Electric Violet (Secondary Feature Accent): `#7C3AED` (Violet 600)
  - Interactive Subtle Tint: `#EEF2FF` (Indigo 50)
- **Status & Feedback Badges:**
  - Emerald (Confirmed / Published / Open RSVP): `#059669` (Text), `#ECFDF5` (Surface)
  - Amber (Waitlist / High Capacity / Reviewing): `#D97706` (Text), `#FFFBEB` (Surface)
  - Rose (Sold Out / Cancelled / Urgent): `#E11D48` (Text), `#FFF1F2` (Surface)
- **Typography & Content:**
  - High-Contrast Text: `#0F172A` (Slate 900)
  - Body Text: `#334155` (Slate 700)
  - Muted / Supporting Labels: `#64748B` (Slate 500)
  - Disabled / Placeholder: `#94A3B8` (Slate 400)

## Typography

The typography strategy leverages three deliberate typefaces to balance contemporary polish, extreme legibility at dense scales, and tactical data presentation.

- **Plus Jakarta Sans:** Expresses structural confidence and warmth for headlines, section titles, and modal headers. Features subtle optical geometric cuts that maintain lightness.
- **Inter:** The backbone for user interface elements, forms, long-form event descriptions, tables, and dialog content. Its neutral, engineered proportions ensure maximum comprehension across varying monitor resolutions.
- **JetBrains Mono:** Dedicated exclusively to metadata stamps, ticket codes, room numbers (`ENG-304`), timestamps (`19:30 EST`), capacity counters (`142/200`), and quick-action keyboard shortcuts (`⌘K`, `⇧E`).

## Layout & Spacing

This design system uses a strict 4px sub-pixel foundation wrapped in a flexible column grid designed for productivity software.

### Layout Architecture
- **Desktop (1280px+):** Fixed collateral navigation sidebar (240px or 64px collapsed), collapsible context panels (320px), and an 8-to-12-column responsive fluid canvas with a maximum inner container constraint of `1440px`. Column gutters remain locked to `gutter-desktop` (1.5rem).
- **Tablet (768px - 1024px):** Off-canvas navigation drawer, single-column main feed with side drawers transforming into modal sheets. Margin set to `margin-tablet` (1.5rem).
- **Mobile (< 768px):** Single vertical stack layout, fixed bottom action tray for primary event conversion (e.g., "RSVP Now"), safe-area-aware gutters at `gutter` (1rem), and margin set to `margin` (1rem).

### Spacing Principles
- Density is prioritized: Use `space-xs` (4px) and `space-sm` (8px) for internal pill padding, chip grouping, and list-item meta tags.
- Structural separation: Use `space-md` (14px) and `space-lg` (20px) inside cards and form modules. Reserving `space-xl` (32px) strictly for section boundaries.

## Elevation & Depth

Visual hierarchy is maintained via fine lines, subtle tonal steps, and diffuse atmospheric shadows rather than heavy drop shadows.

### Elevation Architecture
1. **Level 0 (Base Canvas):** `#F8FAFC` flat surface. No elevation or border.
2. **Level 1 (Card & Module Layer):** `#FFFFFF` surface bounded by a crisp 1px solid `#E2E8F0` border. Shadow: `0px 1px 2px rgba(15, 23, 42, 0.04)`.
3. **Level 2 (Hover & Active Overlay Cards):** Lifted card state. Surface `#FFFFFF`, border `#CBD5E1`. Shadow: `0px 4px 12px -2px rgba(15, 23, 42, 0.06), 0px 2px 4px -1px rgba(15, 23, 42, 0.03)`.
4. **Level 3 (Sticky Headers & Navigation Rails):** Translucent backdrop surface `rgba(255, 255, 255, 0.85)` with `backdrop-filter: blur(12px)` and a bottom border of `1px solid rgba(226, 232, 240, 0.8)`.
5. **Level 4 (Flyouts, Command Palettes `⌘K`, & Dropdowns):** Floating surface `#FFFFFF` with `1px solid #CBD5E1`. Shadow: `0px 10px 25px -5px rgba(15, 23, 42, 0.08), 0px 8px 10px -6px rgba(15, 23, 42, 0.04)`.

## Shapes

The geometric silhouette balances human approachability with software rigor.

- **Standard Containers & Cards:** `rounded-md` (0.5rem / 8px) creates clean borders that nest comfortably inside parent grids without visual friction.
- **Dialogs & Large Modals:** `rounded-lg` (1rem / 16px) for softened focal presence during high-attention flows.
- **Pills & Status Badges:** Fully circular (`rounded-full` / 9999px) for role markers, attendance tags, capacity meters, and category capsules.
- **Action Buttons & Form Controls:** Match standard container curvature at 0.5rem (8px), maintaining uniform horizontal flow.

## Components

### Buttons & Interactive Triggers
- **Primary Button:** Solid `#4F46E5` background, pure white `Inter 500` text, 8px radius. Inset top highlight shadow (`inset 0 1px 0 rgba(255,255,255,0.15)`). Hover transforms to `#4338CA`.
- **Secondary Button:** Surface `#FFFFFF`, border `1px solid #E2E8F0`, text `#334155`. Hover transitions background to `#F8FAFC` and border to `#CBD5E1`.
- **Ghost / Icon Button:** Transparent background, text `#64748B`. Hover introduces `#F1F5F9` background and `#0F172A` icon tint.
- **Command / Shortcut Indicators:** Embedded monospace keys (`JetBrains Mono`, 11px) framed in `#F1F5F9` with a subtle outline (`border-slate-300`).

### Cards (Events, Clubs, Schedules)
- **Structure:** Crisp white background `#FFFFFF`, surrounded by `1px solid #E2E8F0`. Padding set to `1.25rem`.
- **Header Slot:** Event category pill positioned next to an amber/emerald capacity ticker. Monospace timestamp aligned to the far right.
- **Interactive State:** Hover introduces an indigo border accent (`border-indigo-200`) and slight shadow lift (Level 2).

### Chips, Pills & Status Badges
- **Role Tags:** 4px vertical, 8px horizontal padding, `font-mono-micro` styling.
  - *Organizer / Lead:* Light violet tint (`#F5F3FF`), violet text (`#7C3AED`), border `1px solid #DDD6FE`.
  - *Speaker / Guest:* Light blue tint (`#F0F9FF`), blue text (`#0284C7`), border `1px solid #BAE6FD`.
- **Status Badges:** Include a 6px circular indicator dot. Live events pulse with a soft animation.

### Lists & Activity Rows
- **Layout:** Dense, Notion-inspired rows bounded by 1px bottom dividers.
- **Hover State:** Entire row lights up with a subtle slate tint (`#F8FAFC`), revealing hidden contextual quick-action buttons on hover (e.g., bookmark, duplicate, copy link).

### Inputs & Search Form Controls
- **Field Styling:** Height `38px`, background `#FFFFFF`, border `1px solid #E2E8F0`, typography `Inter 14px`.
- **Active State:** Focus ring with `border-color: #4F46E5` and `box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.12)`.
- **Search Bar:** Includes inline leading search icon (`#94A3B8`) and trailing shortcut pill indicator `⌘K`.

### Specialized Product Components
- **Capacity Progress Pill:** A segmented or continuous horizontal bar displaying ticket depletion with clear color transitions: emerald (<70%), amber (70-90%), and rose (>90%).
- **Campus Quick-Switcher:** Compact dropdown menu with university crest thumbnail, active club selector, and keyboard indicator navigation.