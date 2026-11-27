package com.anatomy.flashcard.ui.theme

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.ReadOnlyComposable
import androidx.compose.ui.graphics.Color

// Google Brand Colors
val GoogleBlue = Color(0xFF1A73E8)
val GoogleBlueLight = Color(0xFFD3E3FD)
val GoogleBlueDark = Color(0xFF041E49)

// Dark Theme Primary
val GoogleBlueDarkTheme = Color(0xFFA8C7FA)

// Base Light Colors
val SurfaceLight = Color(0xFFFFFFFF)
val SurfaceVariantLight = Color(0xFFF0F4F9)
val CardBackgroundLight = Color(0xFFFFFFFF)
val CardBorderLight = Color(0xFFE0E3E7)
val TextPrimaryLight = Color(0xFF1F1F1F)
val TextSecondaryLight = Color(0xFF5E5E5E)
val TextTertiaryLight = Color(0xFF8F9193)

// Base Dark Colors
val SurfaceDark = Color(0xFF131314)
val SurfaceVariantDark = Color(0xFF1E1F20)
val CardBackgroundDark = Color(0xFF1E1F20)
val CardBorderDark = Color(0xFF3C4043)
val TextPrimaryDark = Color(0xFFE3E3E3)
val TextSecondaryDark = Color(0xFFC4C7C5)
val TextTertiaryDark = Color(0xFF8E918F)

// Evaluation Colors (Light)
val GotItGreenLight = Color(0xFF188038)
val GotItGreenBgLight = Color(0xFFE6F4EA)
val GotItGreenBorderLight = Color(0xFFCEEAD6)
val MissedItRedLight = Color(0xFFD93025)
val MissedItRedBgLight = Color(0xFFFCE8E6)
val MissedItRedBorderLight = Color(0xFFFAD2CF)

// Evaluation Colors (Dark)
val GotItGreenDark = Color(0xFF81C995)
val GotItGreenBgDark = Color(0xFF0D381E)
val GotItGreenBorderDark = Color(0xFF1B5E20)
val MissedItRedDark = Color(0xFFF28B82)
val MissedItRedBgDark = Color(0xFF3C1614)
val MissedItRedBorderDark = Color(0xFF5C1D1A)

// Backward-compatible static references (default to light or dynamic where appropriate)
val TextPrimary: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) TextPrimaryDark else TextPrimaryLight
val TextSecondary: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) TextSecondaryDark else TextSecondaryLight
val TextTertiary: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) TextTertiaryDark else TextTertiaryLight
val CardBorder: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) CardBorderDark else CardBorderLight
val AppSurface: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) SurfaceDark else SurfaceLight
val AppBackground: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) SurfaceDark else Color(0xFFF9FAFB)
val AppCardBg: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) CardBackgroundDark else Color.White
val CardBackground: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) CardBackgroundDark else CardBackgroundLight
val ChipBg: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) Color(0xFF282A2C) else Color(0xFFF1F3F4)

val GotItGreen: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) GotItGreenDark else GotItGreenLight
val GotItGreenBg: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) GotItGreenBgDark else GotItGreenBgLight
val GotItGreenBorder: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) GotItGreenBorderDark else GotItGreenBorderLight

val MissedItRed: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) MissedItRedDark else MissedItRedLight
val MissedItRedBg: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) MissedItRedBgDark else MissedItRedBgLight
val MissedItRedBorder: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) MissedItRedBorderDark else MissedItRedBorderLight

val CardStackBg1: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) Color(0xFF282A2C) else Color(0xFFF1F3F4)
val CardStackBg2: Color @Composable @ReadOnlyComposable get() = if (isSystemInDarkTheme()) Color(0xFF333538) else Color(0xFFE8EAED)
