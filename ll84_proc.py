#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
A script to process data from LL84 energy and water use benchmarking from
http://www.nyc.gov/html/gbee/html/plan/ll84_scores.shtml
Manually removed column 29 "OwnerName", column 62 "HistDist, and column 63 "Landmark" due to 
formatting errors that caused the file to be parsed incorrectly. They aren't germane to this analysis
"""
import pandas as pd

# download file from internet

# open file
mnplutoFile = open('mn13v1.csv','r')

# iterate and extract
mnplutoList = []
for line in mnplutoFile:
  lineSplit = line.split(",")


# remove duplicates

# remove outliers

# Fields of interest:
# BBL 65
# BldgFront 45
# BldgDepth 46
# NumFloors 40
# NumBldgs  39
# BldgArea  29


next(mnplutoFile) #dump header
for line in mnplutoFile:
    lineSplit = line.split(",")
    cat_bbl = lineSplit[0].strip() + lineSplit[1].strip() + lineSplit[2].strip()
    plutoLineLength.append([cat_bbl, len(lineSplit)])


for line in mnplutoFile:
    lineSplit = line.split(",")
    mnplutoList.append([ lineSplit[68].strip(), lineSplit[44].strip(), lineSplit[45].split(), lineSplit[52].strip() ])

# Borough 0
# Block 1
# Lot 2
# CD  3
# CT2010  4
# CB2010  5
# SchoolDist  6
# Council 7
# ZipCode 8
# FireComp  9
# PolicePrct  10
# Address 11
# ZoneDist1 12
# ZoneDist2 13
# ZoneDist3 14
# ZoneDist4 15
# Overlay1  16
# Overlay2  17
# SPDist1 18
# SPDist2 19
# LtdHeight 20
# AllZoning1  21
# AllZoning2  22
# SplitZone 23
# BldgClass 24
# LandUse 25
# Easements 26
# OwnerType 27
# LotArea 28
# BldgArea  29
# ComArea 30
# ResArea 31
# OfficeArea  32
# RetailArea  33
# GarageArea  34
# StrgeArea 35
# FactryArea  36
# OtherArea 37
# AreaSource  38
# NumBldgs  39
# NumFloors 40
# UnitsRes  41
# UnitsTotal  42
# LotFront  43
# LotDepth  44
# BldgFront 45
# BldgDepth 46
# Ext 47
# ProxCode  48
# IrrLotCode  49
# LotType 50
# BsmtCode  51
# AssessLand  52
# AssessTot 53
# ExemptLand  54
# ExemptTot 55
# YearBuilt 56
# BuiltCode 57
# YearAlter1  58
# YearAlter2  59
# BuiltFAR  60
# ResidFAR  61
# CommFAR 62
# FacilFAR  63
# BoroCode  64
# BBL 65
# CondoNo 66
# Tract2010 67
# XCoord  68
# YCoord  69
# ZoneMap 70
# ZMCode  71
# Sanborn 72
# TaxMap  73
# EDesigNum 74
# APPBBL  75
# APPDate 76
# PLUTOMapID  77
# Version 78


#### Old List ####
# Borough 0
# Block 1
# Lot 2
# CD  3
# CT2010  4
# CB2010  5
# SchoolDist  6
# Council 7
# ZipCode 8
# FireComp  9
# PolicePrct  10
# Address 11
# ZoneDist1 12
# ZoneDist2 13
# ZoneDist3 14
# ZoneDist4 15
# Overlay1  16
# Overlay2  17
# SPDist1 18
# SPDist2 19
# LtdHeight 20
# AllZoning1  21
# AllZoning2  22
# SplitZone 23
# BldgClass 24
# LandUse 25
# Easements 26
# OwnerType 27
# OwnerName 28
# LotArea 29
# BldgArea  30
# ComArea 31
# ResArea 32
# OfficeArea  33
# RetailArea  34
# GarageArea  35
# StrgeArea 36
# FactryArea  37
# OtherArea 38
# AreaSource  39
# NumBldgs  40
# NumFloors 41
# UnitsRes  42
# UnitsTotal  43
# LotFront  44
# LotDepth  45
# BldgFront 46
# BldgDepth 47
# Ext 48
# ProxCode  49
# IrrLotCode  50
# LotType 51
# BsmtCode  52
# AssessLand  53
# AssessTot 54
# ExemptLand  55
# ExemptTot 56
# YearBuilt 57
# BuiltCode 58
# YearAlter1  59
# YearAlter2  60
# HistDist  61
# Landmark  62
# BuiltFAR  63
# ResidFAR  64
# CommFAR 65
# FacilFAR  66
# BoroCode  67
# BBL 68
# CondoNo 69
# Tract2010 70
# XCoord  71
# YCoord  72
# ZoneMap 73
# ZMCode  74
# Sanborn 75
# TaxMap  76
# EDesigNum 77
# APPBBL  78
# APPDate 79
# PLUTOMapID  80
# Version 81