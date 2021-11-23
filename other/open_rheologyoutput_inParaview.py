# -*- coding: utf-8 -*-
"""
Paraview macro to open in Paraview the output from GMS rheology module
"""


# trace generated using paraview version 5.6.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

import os #i 
import glob
import fnmatch # Unix filename pattern matching
from paraview.simple import *
import re # Regular Expression module

path = r'..\output\paraview'


model_name = re.search(r'Rheology(.*?)output', path).group(1) # extract name of the model
model_name = model_name.replace('\\','_' ) # replace \\ by _
model_name = model_name[:-1] # eliminate last _




                        
list_files = os.listdir(path)
list_files = sorted(list_files)


for file in list_files:
        
    # work with constant gridding files
    if fnmatch.fnmatch(file, '*constant*'):
        
        # work with isotherms files
        if fnmatch.fnmatch(file, '*isotherm*'):
            #print(file)
    
            #### import the simple module from the paraview
            
            #### disable automatic camera reset on 'Show'
            paraview.simple._DisableFirstRenderCameraReset()
            
            # create a new 'CSV Reader'
            table = CSVReader(FileName=[path + '\\' + file])
            
            
            # Properties modified on file
            table.FieldDelimiterCharacters = ' '
            
            # get active source.
            cSVReader1 = GetActiveSource()
            
            # rename source object
            RenameSource(file+model_name, cSVReader1)
            
            # find view
            renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
            # uncomment following to set a specific view size
            # renderView1.ViewSize = [754, 942]
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            
            
            # set active view
            SetActiveView(renderView1)
            
            # create a new 'Table To Points'
            tableToPoints11 = TableToPoints(Input=table)
            tableToPoints11.XColumn = 'x'
            tableToPoints11.YColumn = 'y'
            tableToPoints11.ZColumn = 'z'
            
            # show data in view
            tableToPoints11Display = Show(tableToPoints11, renderView1)
            
            # trace defaults for the display properties.
            tableToPoints11Display.Representation = 'Surface'
            tableToPoints11Display.ColorArrayName = [None, '']
            tableToPoints11Display.OSPRayScaleArray = 'temp'
            tableToPoints11Display.OSPRayScaleFunction = 'PiecewiseFunction'
            tableToPoints11Display.SelectOrientationVectors = 'None'
            tableToPoints11Display.ScaleFactor = 110000.0
            tableToPoints11Display.SelectScaleArray = 'None'
            tableToPoints11Display.GlyphType = 'Arrow'
            tableToPoints11Display.GlyphTableIndexArray = 'None'
            tableToPoints11Display.GaussianRadius = 5500.0
            tableToPoints11Display.SetScaleArray = ['POINTS', 'temp']
            tableToPoints11Display.ScaleTransferFunction = 'PiecewiseFunction'
            tableToPoints11Display.OpacityArray = ['POINTS', 'temp']
            tableToPoints11Display.OpacityTransferFunction = 'PiecewiseFunction'
            tableToPoints11Display.DataAxesGrid = 'GridAxesRepresentation'
            tableToPoints11Display.SelectionCellLabelFontFile = ''
            tableToPoints11Display.SelectionPointLabelFontFile = ''
            tableToPoints11Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            tableToPoints11Display.DataAxesGrid.XTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.YTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.ZTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.XLabelFontFile = ''
            tableToPoints11Display.DataAxesGrid.YLabelFontFile = ''
            tableToPoints11Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            tableToPoints11Display.PolarAxes.PolarAxisTitleFontFile = ''
            tableToPoints11Display.PolarAxes.PolarAxisLabelFontFile = ''
            tableToPoints11Display.PolarAxes.LastRadialAxisTextFontFile = ''
            tableToPoints11Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            # create a new 'Delaunay 2D'
            delaunay2D7 = Delaunay2D(Input=tableToPoints11)
            
            # show data in view
            delaunay2D7Display = Show(delaunay2D7, renderView1)
            
            # trace defaults for the display properties.
            delaunay2D7Display.Representation = 'Surface'
            delaunay2D7Display.ColorArrayName = [None, '']
            delaunay2D7Display.OSPRayScaleArray = 'temp'
            delaunay2D7Display.OSPRayScaleFunction = 'PiecewiseFunction'
            delaunay2D7Display.SelectOrientationVectors = 'None'
            delaunay2D7Display.ScaleFactor = 110000.0
            delaunay2D7Display.SelectScaleArray = 'None'
            delaunay2D7Display.GlyphType = 'Arrow'
            delaunay2D7Display.GlyphTableIndexArray = 'None'
            delaunay2D7Display.GaussianRadius = 5500.0
            delaunay2D7Display.SetScaleArray = ['POINTS', 'temp']
            delaunay2D7Display.ScaleTransferFunction = 'PiecewiseFunction'
            delaunay2D7Display.OpacityArray = ['POINTS', 'temp']
            delaunay2D7Display.OpacityTransferFunction = 'PiecewiseFunction'
            delaunay2D7Display.DataAxesGrid = 'GridAxesRepresentation'
            delaunay2D7Display.SelectionCellLabelFontFile = ''
            delaunay2D7Display.SelectionPointLabelFontFile = ''
            delaunay2D7Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            delaunay2D7Display.DataAxesGrid.XTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.YTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.ZTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.XLabelFontFile = ''
            delaunay2D7Display.DataAxesGrid.YLabelFontFile = ''
            delaunay2D7Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            delaunay2D7Display.PolarAxes.PolarAxisTitleFontFile = ''
            delaunay2D7Display.PolarAxes.PolarAxisLabelFontFile = ''
            delaunay2D7Display.PolarAxes.LastRadialAxisTextFontFile = ''
            delaunay2D7Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            # hide data in view
            Hide(tableToPoints11, renderView1)
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            #### saving camera placements for all active views
            
            # current camera placement for renderView1
            renderView1.CameraPosition = [1301860.2725658435, 3224554.241566224, 1935054.1867831652]
            renderView1.CameraFocalPoint = [549999.9999999984, 6249999.999999991, -51403.76196288581]
            renderView1.CameraViewUp = [-0.08921039320574403, 0.5310768386613612, 0.8426143229150161]
            renderView1.CameraParallelScale = 653468.1810686395
            
            # create a new 'Calculator'
            calculator8 = Calculator(Input=delaunay2D7)
            calculator8.Function = ''
            
            # Properties modified on calculator8
            calculator8.ResultArrayName = 'Depth'
            calculator8.Function = 'coordsZ'
            
            # get color transfer function/color map for 'Depth'
            depthLUT = GetColorTransferFunction('Depth')
            
            # show data in view
            calculator8Display = Show(calculator8, renderView1)
            
            # trace defaults for the display properties.
            calculator8Display.Representation = 'Surface'
            calculator8Display.ColorArrayName = ['POINTS', 'Depth']
            calculator8Display.LookupTable = depthLUT
            calculator8Display.OSPRayScaleArray = 'Depth'
            calculator8Display.OSPRayScaleFunction = 'PiecewiseFunction'
            calculator8Display.SelectOrientationVectors = 'Depth'
            calculator8Display.ScaleFactor = 110000.0
            calculator8Display.SelectScaleArray = 'Depth'
            calculator8Display.GlyphType = 'Arrow'
            calculator8Display.GlyphTableIndexArray = 'Depth'
            calculator8Display.GaussianRadius = 5500.0
            calculator8Display.SetScaleArray = ['POINTS', 'Depth']
            calculator8Display.ScaleTransferFunction = 'PiecewiseFunction'
            calculator8Display.OpacityArray = ['POINTS', 'Depth']
            calculator8Display.OpacityTransferFunction = 'PiecewiseFunction'
            calculator8Display.DataAxesGrid = 'GridAxesRepresentation'
            calculator8Display.SelectionCellLabelFontFile = ''
            calculator8Display.SelectionPointLabelFontFile = ''
            calculator8Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            calculator8Display.DataAxesGrid.XTitleFontFile = ''
            calculator8Display.DataAxesGrid.YTitleFontFile = ''
            calculator8Display.DataAxesGrid.ZTitleFontFile = ''
            calculator8Display.DataAxesGrid.XLabelFontFile = ''
            calculator8Display.DataAxesGrid.YLabelFontFile = ''
            calculator8Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            calculator8Display.PolarAxes.PolarAxisTitleFontFile = ''
            calculator8Display.PolarAxes.PolarAxisLabelFontFile = ''
            calculator8Display.PolarAxes.LastRadialAxisTextFontFile = ''
            calculator8Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            
            # show color bar/color legend
            calculator8Display.SetScalarBarVisibility(renderView1, True)
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            # get opacity transfer function/opacity map for 'Depth'
            depthPWF = GetOpacityTransferFunction('Depth')
            
            #### saving camera placements for all active views
            
            # current camera placement for renderView1
            renderView1.CameraPosition = [730640.3449752261, 4396660.089080625, 913101.644208288]
            renderView1.CameraFocalPoint = [724747.8258518912, 6151360.792338837, -211648.05641374787]
            renderView1.CameraViewUp = [-0.023244904582293113, 0.5394451003848643, 0.8416998622322116]
            renderView1.CameraParallelScale = 652724.7291840642
            
        # work with bdt files
        if fnmatch.fnmatch(file, '*bdt*'):
            #print(file)
    
            #### import the simple module from the paraview
            
            #### disable automatic camera reset on 'Show'
            paraview.simple._DisableFirstRenderCameraReset()
            
            # create a new 'CSV Reader'
            table = CSVReader(FileName=[path + '\\' + file])
            
            
            # Properties modified on file
            table.FieldDelimiterCharacters = ' '
            
            # get active source.
            cSVReader1 = GetActiveSource()
            
            # rename source object
            RenameSource(file+model_name, cSVReader1)
            
            # find view
            renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
            # uncomment following to set a specific view size
            # renderView1.ViewSize = [754, 942]
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            
            
            # set active view
            SetActiveView(renderView1)
            
            # create a new 'Table To Points'
            tableToPoints11 = TableToPoints(Input=table)
            tableToPoints11.XColumn = 'x'
            tableToPoints11.YColumn = 'y'
            tableToPoints11.ZColumn = 'bdt'
            
            # show data in view
            tableToPoints11Display = Show(tableToPoints11, renderView1)
            
            # trace defaults for the display properties.
            tableToPoints11Display.Representation = 'Surface'
            tableToPoints11Display.ColorArrayName = [None, '']
            tableToPoints11Display.OSPRayScaleArray = 'temp'
            tableToPoints11Display.OSPRayScaleFunction = 'PiecewiseFunction'
            tableToPoints11Display.SelectOrientationVectors = 'None'
            tableToPoints11Display.ScaleFactor = 110000.0
            tableToPoints11Display.SelectScaleArray = 'None'
            tableToPoints11Display.GlyphType = 'Arrow'
            tableToPoints11Display.GlyphTableIndexArray = 'None'
            tableToPoints11Display.GaussianRadius = 5500.0
            tableToPoints11Display.SetScaleArray = ['POINTS', 'temp']
            tableToPoints11Display.ScaleTransferFunction = 'PiecewiseFunction'
            tableToPoints11Display.OpacityArray = ['POINTS', 'temp']
            tableToPoints11Display.OpacityTransferFunction = 'PiecewiseFunction'
            tableToPoints11Display.DataAxesGrid = 'GridAxesRepresentation'
            tableToPoints11Display.SelectionCellLabelFontFile = ''
            tableToPoints11Display.SelectionPointLabelFontFile = ''
            tableToPoints11Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            tableToPoints11Display.DataAxesGrid.XTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.YTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.ZTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.XLabelFontFile = ''
            tableToPoints11Display.DataAxesGrid.YLabelFontFile = ''
            tableToPoints11Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            tableToPoints11Display.PolarAxes.PolarAxisTitleFontFile = ''
            tableToPoints11Display.PolarAxes.PolarAxisLabelFontFile = ''
            tableToPoints11Display.PolarAxes.LastRadialAxisTextFontFile = ''
            tableToPoints11Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            # create a new 'Delaunay 2D'
            delaunay2D7 = Delaunay2D(Input=tableToPoints11)
            
            # show data in view
            delaunay2D7Display = Show(delaunay2D7, renderView1)
            
            # trace defaults for the display properties.
            delaunay2D7Display.Representation = 'Surface'
            delaunay2D7Display.ColorArrayName = [None, '']
            delaunay2D7Display.OSPRayScaleArray = 'temp'
            delaunay2D7Display.OSPRayScaleFunction = 'PiecewiseFunction'
            delaunay2D7Display.SelectOrientationVectors = 'None'
            delaunay2D7Display.ScaleFactor = 110000.0
            delaunay2D7Display.SelectScaleArray = 'None'
            delaunay2D7Display.GlyphType = 'Arrow'
            delaunay2D7Display.GlyphTableIndexArray = 'None'
            delaunay2D7Display.GaussianRadius = 5500.0
            delaunay2D7Display.SetScaleArray = ['POINTS', 'temp']
            delaunay2D7Display.ScaleTransferFunction = 'PiecewiseFunction'
            delaunay2D7Display.OpacityArray = ['POINTS', 'temp']
            delaunay2D7Display.OpacityTransferFunction = 'PiecewiseFunction'
            delaunay2D7Display.DataAxesGrid = 'GridAxesRepresentation'
            delaunay2D7Display.SelectionCellLabelFontFile = ''
            delaunay2D7Display.SelectionPointLabelFontFile = ''
            delaunay2D7Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            delaunay2D7Display.DataAxesGrid.XTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.YTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.ZTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.XLabelFontFile = ''
            delaunay2D7Display.DataAxesGrid.YLabelFontFile = ''
            delaunay2D7Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            delaunay2D7Display.PolarAxes.PolarAxisTitleFontFile = ''
            delaunay2D7Display.PolarAxes.PolarAxisLabelFontFile = ''
            delaunay2D7Display.PolarAxes.LastRadialAxisTextFontFile = ''
            delaunay2D7Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
    
            
            #### saving camera placements for all active views
            
            # current camera placement for renderView1
            renderView1.CameraPosition = [1301860.2725658435, 3224554.241566224, 1935054.1867831652]
            renderView1.CameraFocalPoint = [549999.9999999984, 6249999.999999991, -51403.76196288581]
            renderView1.CameraViewUp = [-0.08921039320574403, 0.5310768386613612, 0.8426143229150161]
            renderView1.CameraParallelScale = 653468.1810686395        
    
            # create a new 'Calculator'
            calculator8 = Calculator(Input=delaunay2D7)
            calculator8.Function = ''
            
            # Properties modified on calculator8
            calculator8.ResultArrayName = 'Depth'
            calculator8.Function = 'coordsZ'
            
            # get color transfer function/color map for 'Depth'
            depthLUT = GetColorTransferFunction('Depth')
    
            # show data in view
            calculator8Display = Show(calculator8, renderView1)
            
            # trace defaults for the display properties.
            calculator8Display.Representation = 'Surface'
            calculator8Display.ColorArrayName = ['POINTS', 'Depth']
            calculator8Display.LookupTable = depthLUT
            calculator8Display.OSPRayScaleArray = 'Depth'
            calculator8Display.OSPRayScaleFunction = 'PiecewiseFunction'
            calculator8Display.SelectOrientationVectors = 'Depth'
            calculator8Display.ScaleFactor = 110000.0
            calculator8Display.SelectScaleArray = 'Depth'
            calculator8Display.GlyphType = 'Arrow'
            calculator8Display.GlyphTableIndexArray = 'Depth'
            calculator8Display.GaussianRadius = 5500.0
            calculator8Display.SetScaleArray = ['POINTS', 'Depth']
            calculator8Display.ScaleTransferFunction = 'PiecewiseFunction'
            calculator8Display.OpacityArray = ['POINTS', 'Depth']
            calculator8Display.OpacityTransferFunction = 'PiecewiseFunction'
            calculator8Display.DataAxesGrid = 'GridAxesRepresentation'
            calculator8Display.SelectionCellLabelFontFile = ''
            calculator8Display.SelectionPointLabelFontFile = ''
            calculator8Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            calculator8Display.DataAxesGrid.XTitleFontFile = ''
            calculator8Display.DataAxesGrid.YTitleFontFile = ''
            calculator8Display.DataAxesGrid.ZTitleFontFile = ''
            calculator8Display.DataAxesGrid.XLabelFontFile = ''
            calculator8Display.DataAxesGrid.YLabelFontFile = ''
            calculator8Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            calculator8Display.PolarAxes.PolarAxisTitleFontFile = ''
            calculator8Display.PolarAxes.PolarAxisLabelFontFile = ''
            calculator8Display.PolarAxes.LastRadialAxisTextFontFile = ''
            calculator8Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            
            # show color bar/color legend
            calculator8Display.SetScalarBarVisibility(renderView1, True)
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            # get opacity transfer function/opacity map for 'Depth'
            depthPWF = GetOpacityTransferFunction('Depth')
            
            #### saving camera placements for all active views
            
            # current camera placement for renderView1
            renderView1.CameraPosition = [730640.3449752261, 4396660.089080625, 913101.644208288]
            renderView1.CameraFocalPoint = [724747.8258518912, 6151360.792338837, -211648.05641374787]
            renderView1.CameraViewUp = [-0.023244904582293113, 0.5394451003848643, 0.8416998622322116]
            renderView1.CameraParallelScale = 652724.7291840642
    
        # work with bdt files
        if fnmatch.fnmatch(file, '*strength*'):
            #print(file)
    
            #### import the simple module from the paraview
            
            #### disable automatic camera reset on 'Show'
            paraview.simple._DisableFirstRenderCameraReset()
            
            # create a new 'CSV Reader'
            table = CSVReader(FileName=[path + '\\' + file])
            
            
            # Properties modified on file
            table.FieldDelimiterCharacters = ' '
            
            # get active source.
            cSVReader1 = GetActiveSource()
            
            # rename source object
            RenameSource(file+model_name, cSVReader1)
            
            # find view
            renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
            # uncomment following to set a specific view size
            # renderView1.ViewSize = [754, 942]
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            
            
            # set active view
            SetActiveView(renderView1)
            
            ## total strength
            
            # create a new 'Table To Points' (total strength)
            tableToPoints11 = TableToPoints(Input=table)
            tableToPoints11.XColumn = 'x'
            tableToPoints11.YColumn = 'y'
            tableToPoints11.ZColumn = 'log_total_strength'
            
            # show data in view
            tableToPoints11Display = Show(tableToPoints11, renderView1)
            
            # trace defaults for the display properties.
            tableToPoints11Display.Representation = 'Surface'
            tableToPoints11Display.ColorArrayName = [None, '']
            tableToPoints11Display.OSPRayScaleArray = 'log_total_strength'
            tableToPoints11Display.OSPRayScaleFunction = 'PiecewiseFunction'
            tableToPoints11Display.SelectOrientationVectors = 'None'
            tableToPoints11Display.ScaleFactor = 110000.0
            tableToPoints11Display.SelectScaleArray = 'None'
            tableToPoints11Display.GlyphType = 'Arrow'
            tableToPoints11Display.GlyphTableIndexArray = 'None'
            tableToPoints11Display.GaussianRadius = 5500.0
            tableToPoints11Display.SetScaleArray = ['POINTS', 'log_total_strength']
            tableToPoints11Display.ScaleTransferFunction = 'PiecewiseFunction'
            tableToPoints11Display.OpacityArray = ['POINTS', 'log_total_strength']
            tableToPoints11Display.OpacityTransferFunction = 'PiecewiseFunction'
            tableToPoints11Display.DataAxesGrid = 'GridAxesRepresentation'
            tableToPoints11Display.SelectionCellLabelFontFile = ''
            tableToPoints11Display.SelectionPointLabelFontFile = ''
            tableToPoints11Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            tableToPoints11Display.DataAxesGrid.XTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.YTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.ZTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.XLabelFontFile = ''
            tableToPoints11Display.DataAxesGrid.YLabelFontFile = ''
            tableToPoints11Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            tableToPoints11Display.PolarAxes.PolarAxisTitleFontFile = ''
            tableToPoints11Display.PolarAxes.PolarAxisLabelFontFile = ''
            tableToPoints11Display.PolarAxes.LastRadialAxisTextFontFile = ''
            tableToPoints11Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
    
    
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            # create a new 'Delaunay 2D'
            delaunay2D7 = Delaunay2D(Input=tableToPoints11)
            
            # show data in view
            delaunay2D7Display = Show(delaunay2D7, renderView1)
            
            # trace defaults for the display properties.
            delaunay2D7Display.Representation = 'Surface'
            delaunay2D7Display.ColorArrayName = [None, '']
            delaunay2D7Display.OSPRayScaleArray = 'log_total_strength'
            delaunay2D7Display.OSPRayScaleFunction = 'PiecewiseFunction'
            delaunay2D7Display.SelectOrientationVectors = 'None'
            delaunay2D7Display.ScaleFactor = 110000.0
            delaunay2D7Display.SelectScaleArray = 'None'
            delaunay2D7Display.GlyphType = 'Arrow'
            delaunay2D7Display.GlyphTableIndexArray = 'None'
            delaunay2D7Display.GaussianRadius = 5500.0
            delaunay2D7Display.SetScaleArray = ['POINTS', 'log_total_strength']
            delaunay2D7Display.ScaleTransferFunction = 'PiecewiseFunction'
            delaunay2D7Display.OpacityArray = ['POINTS', 'log_total_strength']
            delaunay2D7Display.OpacityTransferFunction = 'PiecewiseFunction'
            delaunay2D7Display.DataAxesGrid = 'GridAxesRepresentation'
            delaunay2D7Display.SelectionCellLabelFontFile = ''
            delaunay2D7Display.SelectionPointLabelFontFile = ''
            delaunay2D7Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            delaunay2D7Display.DataAxesGrid.XTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.YTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.ZTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.XLabelFontFile = ''
            delaunay2D7Display.DataAxesGrid.YLabelFontFile = ''
            delaunay2D7Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            delaunay2D7Display.PolarAxes.PolarAxisTitleFontFile = ''
            delaunay2D7Display.PolarAxes.PolarAxisLabelFontFile = ''
            delaunay2D7Display.PolarAxes.LastRadialAxisTextFontFile = ''
            delaunay2D7Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            # hide data in view
            Hide(tableToPoints11, renderView1)
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            
            #### saving camera placements for all active views
            
            # current camera placement for renderView1
            renderView1.CameraPosition = [1301860.2725658435, 3224554.241566224, 1935054.1867831652]
            renderView1.CameraFocalPoint = [549999.9999999984, 6249999.999999991, -51403.76196288581]
            renderView1.CameraViewUp = [-0.08921039320574403, 0.5310768386613612, 0.8426143229150161]
            renderView1.CameraParallelScale = 653468.1810686395
            
            # create a new 'Calculator'
            calculator8 = Calculator(Input=delaunay2D7)
            calculator8.Function = ''
            
            # Properties modified on calculator8
            calculator8.ResultArrayName = 'Log_total_strength'
            calculator8.Function = 'coordsZ'
            
            # get color transfer function/color map for 'Log_total_strength'
            depthLUT = GetColorTransferFunction('Log_total_strength')
            
            # show data in view
            calculator8Display = Show(calculator8, renderView1)
            
            # trace defaults for the display properties.
            calculator8Display.Representation = 'Surface'
            calculator8Display.ColorArrayName = ['POINTS', 'Log_total_strength']
            calculator8Display.LookupTable = depthLUT
            calculator8Display.OSPRayScaleArray = 'Log_total_strength'
            calculator8Display.OSPRayScaleFunction = 'PiecewiseFunction'
            calculator8Display.SelectOrientationVectors = 'Log_total_strength'
            calculator8Display.ScaleFactor = 110000.0
            calculator8Display.SelectScaleArray = 'Log_total_strengthh'
            calculator8Display.GlyphType = 'Arrow'
            calculator8Display.GlyphTableIndexArray = 'Log_total_strength'
            calculator8Display.GaussianRadius = 5500.0
            calculator8Display.SetScaleArray = ['POINTS', 'Log_total_strength']
            calculator8Display.ScaleTransferFunction = 'PiecewiseFunction'
            calculator8Display.OpacityArray = ['POINTS', 'Log_total_strength']
            calculator8Display.OpacityTransferFunction = 'PiecewiseFunction'
            calculator8Display.DataAxesGrid = 'GridAxesRepresentation'
            calculator8Display.SelectionCellLabelFontFile = ''
            calculator8Display.SelectionPointLabelFontFile = ''
            calculator8Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            calculator8Display.DataAxesGrid.XTitleFontFile = ''
            calculator8Display.DataAxesGrid.YTitleFontFile = ''
            calculator8Display.DataAxesGrid.ZTitleFontFile = ''
            calculator8Display.DataAxesGrid.XLabelFontFile = ''
            calculator8Display.DataAxesGrid.YLabelFontFile = ''
            calculator8Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            calculator8Display.PolarAxes.PolarAxisTitleFontFile = ''
            calculator8Display.PolarAxes.PolarAxisLabelFontFile = ''
            calculator8Display.PolarAxes.LastRadialAxisTextFontFile = ''
            calculator8Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            
            # show color bar/color legend
            calculator8Display.SetScalarBarVisibility(renderView1, True)
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            # get opacity transfer function/opacity map for 'Log_total_strength'
            depthPWF = GetOpacityTransferFunction('Log_total_strength')
            
            #### saving camera placements for all active views
            
            # current camera placement for renderView1
            renderView1.CameraPosition = [730640.3449752261, 4396660.089080625, 913101.644208288]
            renderView1.CameraFocalPoint = [724747.8258518912, 6151360.792338837, -211648.05641374787]
            renderView1.CameraViewUp = [-0.023244904582293113, 0.5394451003848643, 0.8416998622322116]
            renderView1.CameraParallelScale = 652724.7291840642
            
            # rename source object
            RenameSource('log_total_strength', tableToPoints11)
            
            ## crustal strength
            
            # create a new 'Table To Points' (log_crustal_strength)
            tableToPoints11 = TableToPoints(Input=table)
            tableToPoints11.XColumn = 'x'
            tableToPoints11.YColumn = 'y'
            tableToPoints11.ZColumn = 'log_crustal_strength'
            
            # show data in view
            tableToPoints11Display = Show(tableToPoints11, renderView1)
            
            # trace defaults for the display properties.
            tableToPoints11Display.Representation = 'Surface'
            tableToPoints11Display.ColorArrayName = [None, '']
            tableToPoints11Display.OSPRayScaleArray = 'log_crustal_strength'
            tableToPoints11Display.OSPRayScaleFunction = 'PiecewiseFunction'
            tableToPoints11Display.SelectOrientationVectors = 'None'
            tableToPoints11Display.ScaleFactor = 110000.0
            tableToPoints11Display.SelectScaleArray = 'None'
            tableToPoints11Display.GlyphType = 'Arrow'
            tableToPoints11Display.GlyphTableIndexArray = 'None'
            tableToPoints11Display.GaussianRadius = 5500.0
            tableToPoints11Display.SetScaleArray = ['POINTS', 'log_crustal_strength']
            tableToPoints11Display.ScaleTransferFunction = 'PiecewiseFunction'
            tableToPoints11Display.OpacityArray = ['POINTS', 'log_crustal_strength']
            tableToPoints11Display.OpacityTransferFunction = 'PiecewiseFunction'
            tableToPoints11Display.DataAxesGrid = 'GridAxesRepresentation'
            tableToPoints11Display.SelectionCellLabelFontFile = ''
            tableToPoints11Display.SelectionPointLabelFontFile = ''
            tableToPoints11Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            tableToPoints11Display.DataAxesGrid.XTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.YTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.ZTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.XLabelFontFile = ''
            tableToPoints11Display.DataAxesGrid.YLabelFontFile = ''
            tableToPoints11Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            tableToPoints11Display.PolarAxes.PolarAxisTitleFontFile = ''
            tableToPoints11Display.PolarAxes.PolarAxisLabelFontFile = ''
            tableToPoints11Display.PolarAxes.LastRadialAxisTextFontFile = ''
            tableToPoints11Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
    
    
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            # create a new 'Delaunay 2D'
            delaunay2D7 = Delaunay2D(Input=tableToPoints11)
            
            # show data in view
            delaunay2D7Display = Show(delaunay2D7, renderView1)
            
            # trace defaults for the display properties.
            delaunay2D7Display.Representation = 'Surface'
            delaunay2D7Display.ColorArrayName = [None, '']
            delaunay2D7Display.OSPRayScaleArray = 'log_crustal_strength'
            delaunay2D7Display.OSPRayScaleFunction = 'PiecewiseFunction'
            delaunay2D7Display.SelectOrientationVectors = 'None'
            delaunay2D7Display.ScaleFactor = 110000.0
            delaunay2D7Display.SelectScaleArray = 'None'
            delaunay2D7Display.GlyphType = 'Arrow'
            delaunay2D7Display.GlyphTableIndexArray = 'None'
            delaunay2D7Display.GaussianRadius = 5500.0
            delaunay2D7Display.SetScaleArray = ['POINTS', 'log_crustal_strength']
            delaunay2D7Display.ScaleTransferFunction = 'PiecewiseFunction'
            delaunay2D7Display.OpacityArray = ['POINTS', 'log_crustal_strength']
            delaunay2D7Display.OpacityTransferFunction = 'PiecewiseFunction'
            delaunay2D7Display.DataAxesGrid = 'GridAxesRepresentation'
            delaunay2D7Display.SelectionCellLabelFontFile = ''
            delaunay2D7Display.SelectionPointLabelFontFile = ''
            delaunay2D7Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            delaunay2D7Display.DataAxesGrid.XTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.YTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.ZTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.XLabelFontFile = ''
            delaunay2D7Display.DataAxesGrid.YLabelFontFile = ''
            delaunay2D7Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            delaunay2D7Display.PolarAxes.PolarAxisTitleFontFile = ''
            delaunay2D7Display.PolarAxes.PolarAxisLabelFontFile = ''
            delaunay2D7Display.PolarAxes.LastRadialAxisTextFontFile = ''
            delaunay2D7Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            # hide data in view
            Hide(tableToPoints11, renderView1)
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            #### saving camera placements for all active views
            
            # current camera placement for renderView1
            renderView1.CameraPosition = [1301860.2725658435, 3224554.241566224, 1935054.1867831652]
            renderView1.CameraFocalPoint = [549999.9999999984, 6249999.999999991, -51403.76196288581]
            renderView1.CameraViewUp = [-0.08921039320574403, 0.5310768386613612, 0.8426143229150161]
            renderView1.CameraParallelScale = 653468.1810686395
            
            # create a new 'Calculator'
            calculator8 = Calculator(Input=delaunay2D7)
            calculator8.Function = ''
            
            # Properties modified on calculator8
            calculator8.ResultArrayName = 'Log_crustal_strength'
            calculator8.Function = 'coordsZ'
            
            # get color transfer function/color map for 'Log_crustal_strength'
            depthLUT = GetColorTransferFunction('Log_crustal_strength')
    
            # show data in view
            calculator8Display = Show(calculator8, renderView1)
            
            # trace defaults for the display properties.
            calculator8Display.Representation = 'Surface'
            calculator8Display.ColorArrayName = ['POINTS', 'Log_crustal_strength']
            calculator8Display.LookupTable = depthLUT
            calculator8Display.OSPRayScaleArray = 'Log_crustal_strength'
            calculator8Display.OSPRayScaleFunction = 'PiecewiseFunction'
            calculator8Display.SelectOrientationVectors = 'Log_crustal_strength'
            calculator8Display.ScaleFactor = 110000.0
            calculator8Display.SelectScaleArray = 'Log_crustal_strengthh'
            calculator8Display.GlyphType = 'Arrow'
            calculator8Display.GlyphTableIndexArray = 'Log_crustal_strength'
            calculator8Display.GaussianRadius = 5500.0
            calculator8Display.SetScaleArray = ['POINTS', 'Log_crustal_strength']
            calculator8Display.ScaleTransferFunction = 'PiecewiseFunction'
            calculator8Display.OpacityArray = ['POINTS', 'Log_crustal_strength']
            calculator8Display.OpacityTransferFunction = 'PiecewiseFunction'
            calculator8Display.DataAxesGrid = 'GridAxesRepresentation'
            calculator8Display.SelectionCellLabelFontFile = ''
            calculator8Display.SelectionPointLabelFontFile = ''
            calculator8Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            calculator8Display.DataAxesGrid.XTitleFontFile = ''
            calculator8Display.DataAxesGrid.YTitleFontFile = ''
            calculator8Display.DataAxesGrid.ZTitleFontFile = ''
            calculator8Display.DataAxesGrid.XLabelFontFile = ''
            calculator8Display.DataAxesGrid.YLabelFontFile = ''
            calculator8Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            calculator8Display.PolarAxes.PolarAxisTitleFontFile = ''
            calculator8Display.PolarAxes.PolarAxisLabelFontFile = ''
            calculator8Display.PolarAxes.LastRadialAxisTextFontFile = ''
            calculator8Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            
            # show color bar/color legend
            calculator8Display.SetScalarBarVisibility(renderView1, True)
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            # get opacity transfer function/opacity map for 'Log_crustal_strength'
            depthPWF = GetOpacityTransferFunction('Log_crustal_strength')
            
            #### saving camera placements for all active views
            
            # current camera placement for renderView1
            renderView1.CameraPosition = [730640.3449752261, 4396660.089080625, 913101.644208288]
            renderView1.CameraFocalPoint = [724747.8258518912, 6151360.792338837, -211648.05641374787]
            renderView1.CameraViewUp = [-0.023244904582293113, 0.5394451003848643, 0.8416998622322116]
            renderView1.CameraParallelScale = 652724.7291840642
            
            # rename source object
            RenameSource('Log_crustal_strength', tableToPoints11)
            
            ## strength ratio
            # create a new 'Table To Points' (strength_ratio)
            tableToPoints11 = TableToPoints(Input=table)
            tableToPoints11.XColumn = 'x'
            tableToPoints11.YColumn = 'y'
            tableToPoints11.ZColumn = 'strength_ratio'
            
            # show data in view
            tableToPoints11Display = Show(tableToPoints11, renderView1)
            
            # trace defaults for the display properties.
            tableToPoints11Display.Representation = 'Surface'
            tableToPoints11Display.ColorArrayName = [None, '']
            tableToPoints11Display.OSPRayScaleArray = 'strength_ratio'
            tableToPoints11Display.OSPRayScaleFunction = 'PiecewiseFunction'
            tableToPoints11Display.SelectOrientationVectors = 'None'
            tableToPoints11Display.ScaleFactor = 110000.0
            tableToPoints11Display.SelectScaleArray = 'None'
            tableToPoints11Display.GlyphType = 'Arrow'
            tableToPoints11Display.GlyphTableIndexArray = 'None'
            tableToPoints11Display.GaussianRadius = 5500.0
            tableToPoints11Display.SetScaleArray = ['POINTS', 'strength_ratio']
            tableToPoints11Display.ScaleTransferFunction = 'PiecewiseFunction'
            tableToPoints11Display.OpacityArray = ['POINTS', 'strength_ratio']
            tableToPoints11Display.OpacityTransferFunction = 'PiecewiseFunction'
            tableToPoints11Display.DataAxesGrid = 'GridAxesRepresentation'
            tableToPoints11Display.SelectionCellLabelFontFile = ''
            tableToPoints11Display.SelectionPointLabelFontFile = ''
            tableToPoints11Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            tableToPoints11Display.DataAxesGrid.XTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.YTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.ZTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.XLabelFontFile = ''
            tableToPoints11Display.DataAxesGrid.YLabelFontFile = ''
            tableToPoints11Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            tableToPoints11Display.PolarAxes.PolarAxisTitleFontFile = ''
            tableToPoints11Display.PolarAxes.PolarAxisLabelFontFile = ''
            tableToPoints11Display.PolarAxes.LastRadialAxisTextFontFile = ''
            tableToPoints11Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
    
    
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            # create a new 'Delaunay 2D'
            delaunay2D7 = Delaunay2D(Input=tableToPoints11)
            
            # show data in view
            delaunay2D7Display = Show(delaunay2D7, renderView1)
            
            # trace defaults for the display properties.
            delaunay2D7Display.Representation = 'Surface'
            delaunay2D7Display.ColorArrayName = [None, '']
            delaunay2D7Display.OSPRayScaleArray = 'strength_ratio'
            delaunay2D7Display.OSPRayScaleFunction = 'PiecewiseFunction'
            delaunay2D7Display.SelectOrientationVectors = 'None'
            delaunay2D7Display.ScaleFactor = 110000.0
            delaunay2D7Display.SelectScaleArray = 'None'
            delaunay2D7Display.GlyphType = 'Arrow'
            delaunay2D7Display.GlyphTableIndexArray = 'None'
            delaunay2D7Display.GaussianRadius = 5500.0
            delaunay2D7Display.SetScaleArray = ['POINTS', 'strength_ratio']
            delaunay2D7Display.ScaleTransferFunction = 'PiecewiseFunction'
            delaunay2D7Display.OpacityArray = ['POINTS', 'strength_ratio']
            delaunay2D7Display.OpacityTransferFunction = 'PiecewiseFunction'
            delaunay2D7Display.DataAxesGrid = 'GridAxesRepresentation'
            delaunay2D7Display.SelectionCellLabelFontFile = ''
            delaunay2D7Display.SelectionPointLabelFontFile = ''
            delaunay2D7Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            delaunay2D7Display.DataAxesGrid.XTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.YTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.ZTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.XLabelFontFile = ''
            delaunay2D7Display.DataAxesGrid.YLabelFontFile = ''
            delaunay2D7Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            delaunay2D7Display.PolarAxes.PolarAxisTitleFontFile = ''
            delaunay2D7Display.PolarAxes.PolarAxisLabelFontFile = ''
            delaunay2D7Display.PolarAxes.LastRadialAxisTextFontFile = ''
            delaunay2D7Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            # hide data in view
            Hide(tableToPoints11, renderView1)
            
            # update the view to ensure updated data information
            renderView1.Update()
    
            #### saving camera placements for all active views
            
            # current camera placement for renderView1
            renderView1.CameraPosition = [1301860.2725658435, 3224554.241566224, 1935054.1867831652]
            renderView1.CameraFocalPoint = [549999.9999999984, 6249999.999999991, -51403.76196288581]
            renderView1.CameraViewUp = [-0.08921039320574403, 0.5310768386613612, 0.8426143229150161]
            renderView1.CameraParallelScale = 653468.1810686395
            
            # create a new 'Calculator'
            calculator8 = Calculator(Input=delaunay2D7)
            calculator8.Function = ''
            
            # Properties modified on calculator8
            calculator8.ResultArrayName = 'strength_ratio'
            calculator8.Function = 'coordsZ'
            
            # get color transfer function/color map for 'strength_ratio'
            depthLUT = GetColorTransferFunction('strength_ratio')
    
            # show data in view
            calculator8Display = Show(calculator8, renderView1)
            
            # trace defaults for the display properties.
            calculator8Display.Representation = 'Surface'
            calculator8Display.ColorArrayName = ['POINTS', 'strength_ratio']
            calculator8Display.LookupTable = depthLUT
            calculator8Display.OSPRayScaleArray = 'strength_ratio'
            calculator8Display.OSPRayScaleFunction = 'PiecewiseFunction'
            calculator8Display.SelectOrientationVectors = 'strength_ratio'
            calculator8Display.ScaleFactor = 110000.0
            calculator8Display.SelectScaleArray = 'strength_ratio'
            calculator8Display.GlyphType = 'Arrow'
            calculator8Display.GlyphTableIndexArray = 'strength_ratio'
            calculator8Display.GaussianRadius = 5500.0
            calculator8Display.SetScaleArray = ['POINTS', 'strength_ratio']
            calculator8Display.ScaleTransferFunction = 'PiecewiseFunction'
            calculator8Display.OpacityArray = ['POINTS', 'strength_ratio']
            calculator8Display.OpacityTransferFunction = 'PiecewiseFunction'
            calculator8Display.DataAxesGrid = 'GridAxesRepresentation'
            calculator8Display.SelectionCellLabelFontFile = ''
            calculator8Display.SelectionPointLabelFontFile = ''
            calculator8Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            calculator8Display.DataAxesGrid.XTitleFontFile = ''
            calculator8Display.DataAxesGrid.YTitleFontFile = ''
            calculator8Display.DataAxesGrid.ZTitleFontFile = ''
            calculator8Display.DataAxesGrid.XLabelFontFile = ''
            calculator8Display.DataAxesGrid.YLabelFontFile = ''
            calculator8Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            calculator8Display.PolarAxes.PolarAxisTitleFontFile = ''
            calculator8Display.PolarAxes.PolarAxisLabelFontFile = ''
            calculator8Display.PolarAxes.LastRadialAxisTextFontFile = ''
            calculator8Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            
            # show color bar/color legend
            calculator8Display.SetScalarBarVisibility(renderView1, True)
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            # get opacity transfer function/opacity map for 'strength_ratio'
            depthPWF = GetOpacityTransferFunction('strength_ratio')
            
            #### saving camera placements for all active views
            
            # current camera placement for renderView1
            renderView1.CameraPosition = [730640.3449752261, 4396660.089080625, 913101.644208288]
            renderView1.CameraFocalPoint = [724747.8258518912, 6151360.792338837, -211648.05641374787]
            renderView1.CameraViewUp = [-0.023244904582293113, 0.5394451003848643, 0.8416998622322116]
            renderView1.CameraParallelScale = 652724.7291840642
            
            # rename source object
            RenameSource('strength_ratio', tableToPoints11)
            
            ## mechanical thickness
            
            # create a new 'Table To Points' (mechanical thickness)
            tableToPoints11 = TableToPoints(Input=table)
            tableToPoints11.XColumn = 'x'
            tableToPoints11.YColumn = 'y'
            tableToPoints11.ZColumn = 'mechanical_thickness'
            
            # show data in view
            tableToPoints11Display = Show(tableToPoints11, renderView1)
            
            # trace defaults for the display properties.
            tableToPoints11Display.Representation = 'Surface'
            tableToPoints11Display.ColorArrayName = [None, '']
            tableToPoints11Display.OSPRayScaleArray = 'mechanical_thickness'
            tableToPoints11Display.OSPRayScaleFunction = 'PiecewiseFunction'
            tableToPoints11Display.SelectOrientationVectors = 'None'
            tableToPoints11Display.ScaleFactor = 110000.0
            tableToPoints11Display.SelectScaleArray = 'None'
            tableToPoints11Display.GlyphType = 'Arrow'
            tableToPoints11Display.GlyphTableIndexArray = 'None'
            tableToPoints11Display.GaussianRadius = 5500.0
            tableToPoints11Display.SetScaleArray = ['POINTS', 'mechanical_thickness']
            tableToPoints11Display.ScaleTransferFunction = 'PiecewiseFunction'
            tableToPoints11Display.OpacityArray = ['POINTS', 'mechanical thickness']
            tableToPoints11Display.OpacityTransferFunction = 'PiecewiseFunction'
            tableToPoints11Display.DataAxesGrid = 'GridAxesRepresentation'
            tableToPoints11Display.SelectionCellLabelFontFile = ''
            tableToPoints11Display.SelectionPointLabelFontFile = ''
            tableToPoints11Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            tableToPoints11Display.DataAxesGrid.XTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.YTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.ZTitleFontFile = ''
            tableToPoints11Display.DataAxesGrid.XLabelFontFile = ''
            tableToPoints11Display.DataAxesGrid.YLabelFontFile = ''
            tableToPoints11Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            tableToPoints11Display.PolarAxes.PolarAxisTitleFontFile = ''
            tableToPoints11Display.PolarAxes.PolarAxisLabelFontFile = ''
            tableToPoints11Display.PolarAxes.LastRadialAxisTextFontFile = ''
            tableToPoints11Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
    
    
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            # create a new 'Delaunay 2D'
            delaunay2D7 = Delaunay2D(Input=tableToPoints11)
            
            # show data in view
            delaunay2D7Display = Show(delaunay2D7, renderView1)
            
            # trace defaults for the display properties.
            delaunay2D7Display.Representation = 'Surface'
            delaunay2D7Display.ColorArrayName = [None, '']
            delaunay2D7Display.OSPRayScaleArray = 'mechanical_thickness'
            delaunay2D7Display.OSPRayScaleFunction = 'PiecewiseFunction'
            delaunay2D7Display.SelectOrientationVectors = 'None'
            delaunay2D7Display.ScaleFactor = 110000.0
            delaunay2D7Display.SelectScaleArray = 'None'
            delaunay2D7Display.GlyphType = 'Arrow'
            delaunay2D7Display.GlyphTableIndexArray = 'None'
            delaunay2D7Display.GaussianRadius = 5500.0
            delaunay2D7Display.SetScaleArray = ['POINTS', 'mechanical_thickness']
            delaunay2D7Display.ScaleTransferFunction = 'PiecewiseFunction'
            delaunay2D7Display.OpacityArray = ['POINTS', 'mechanical_thickness']
            delaunay2D7Display.OpacityTransferFunction = 'PiecewiseFunction'
            delaunay2D7Display.DataAxesGrid = 'GridAxesRepresentation'
            delaunay2D7Display.SelectionCellLabelFontFile = ''
            delaunay2D7Display.SelectionPointLabelFontFile = ''
            delaunay2D7Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            delaunay2D7Display.DataAxesGrid.XTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.YTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.ZTitleFontFile = ''
            delaunay2D7Display.DataAxesGrid.XLabelFontFile = ''
            delaunay2D7Display.DataAxesGrid.YLabelFontFile = ''
            delaunay2D7Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            delaunay2D7Display.PolarAxes.PolarAxisTitleFontFile = ''
            delaunay2D7Display.PolarAxes.PolarAxisLabelFontFile = ''
            delaunay2D7Display.PolarAxes.LastRadialAxisTextFontFile = ''
            delaunay2D7Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            # hide data in view
            Hide(tableToPoints11, renderView1)
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            #### saving camera placements for all active views
            
            # current camera placement for renderView1
            renderView1.CameraPosition = [1301860.2725658435, 3224554.241566224, 1935054.1867831652]
            renderView1.CameraFocalPoint = [549999.9999999984, 6249999.999999991, -51403.76196288581]
            renderView1.CameraViewUp = [-0.08921039320574403, 0.5310768386613612, 0.8426143229150161]
            renderView1.CameraParallelScale = 653468.1810686395
            
            # create a new 'Calculator'
            calculator8 = Calculator(Input=delaunay2D7)
            calculator8.Function = ''
            
            # Properties modified on calculator8
            calculator8.ResultArrayName = 'Mechanical_thickness'
            calculator8.Function = 'coordsZ'
            
            # get color transfer function/color map for 'Mechanical_thickness'
            depthLUT = GetColorTransferFunction('Mechanical_thickness')
            
            # show data in view
            calculator8Display = Show(calculator8, renderView1)
            
            # trace defaults for the display properties.
            calculator8Display.Representation = 'Surface'
            calculator8Display.ColorArrayName = ['POINTS', 'Mechanical_thickness']
            calculator8Display.LookupTable = depthLUT
            calculator8Display.OSPRayScaleArray = 'Mechanical_thickness'
            calculator8Display.OSPRayScaleFunction = 'PiecewiseFunction'
            calculator8Display.SelectOrientationVectors = 'Mechanical_thickness'
            calculator8Display.ScaleFactor = 110000.0
            calculator8Display.SelectScaleArray = 'Mechanical_thickness'
            calculator8Display.GlyphType = 'Arrow'
            calculator8Display.GlyphTableIndexArray = 'Mechanical_thickness'
            calculator8Display.GaussianRadius = 5500.0
            calculator8Display.SetScaleArray = ['POINTS', 'Mechanical_thickness']
            calculator8Display.ScaleTransferFunction = 'PiecewiseFunction'
            calculator8Display.OpacityArray = ['POINTS', 'Mechanical_thickness']
            calculator8Display.OpacityTransferFunction = 'PiecewiseFunction'
            calculator8Display.DataAxesGrid = 'GridAxesRepresentation'
            calculator8Display.SelectionCellLabelFontFile = ''
            calculator8Display.SelectionPointLabelFontFile = ''
            calculator8Display.PolarAxes = 'PolarAxesRepresentation'
            
            # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
            calculator8Display.DataAxesGrid.XTitleFontFile = ''
            calculator8Display.DataAxesGrid.YTitleFontFile = ''
            calculator8Display.DataAxesGrid.ZTitleFontFile = ''
            calculator8Display.DataAxesGrid.XLabelFontFile = ''
            calculator8Display.DataAxesGrid.YLabelFontFile = ''
            calculator8Display.DataAxesGrid.ZLabelFontFile = ''
            
            # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
            calculator8Display.PolarAxes.PolarAxisTitleFontFile = ''
            calculator8Display.PolarAxes.PolarAxisLabelFontFile = ''
            calculator8Display.PolarAxes.LastRadialAxisTextFontFile = ''
            calculator8Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
            
            
            # show color bar/color legend
            calculator8Display.SetScalarBarVisibility(renderView1, True)
            
            # update the view to ensure updated data information
            renderView1.Update()
            
            # get opacity transfer function/opacity map for 'Mechanical_thickness'
            depthPWF = GetOpacityTransferFunction('Mechanical_thickness')
            
            #### saving camera placements for all active views
            
            # current camera placement for renderView1
            renderView1.CameraPosition = [730640.3449752261, 4396660.089080625, 913101.644208288]
            renderView1.CameraFocalPoint = [724747.8258518912, 6151360.792338837, -211648.05641374787]
            renderView1.CameraViewUp = [-0.023244904582293113, 0.5394451003848643, 0.8416998622322116]
            renderView1.CameraParallelScale = 652724.7291840642
            
            # rename source object
            RenameSource('mechanical_thickness', tableToPoints11)
            
    #### uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).