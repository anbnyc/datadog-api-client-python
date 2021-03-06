# Dashboard

A dashboard is Datadog’s tool for visually tracking, analyzing, and displaying key performance metrics, which enable you to monitor the health of your infrastructure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout_type** | [**DashboardLayoutType**](DashboardLayoutType.md) |  | 
**title** | **str** | Title of the dashboard. | 
**widgets** | [**[Widget]**](Widget.md) | List of widgets to display on the dashboard. | 
**author_handle** | **str** | Identifier of the dashboard author. | [optional] [readonly] 
**created_at** | **datetime** | Creation date of the dashboard. | [optional] [readonly] 
**description** | **str, none_type** | Description of the dashboard. | [optional] 
**id** | **str** | ID of the dashboard. | [optional] [readonly] 
**is_read_only** | **bool** | Whether this dashboard is read-only. If True, only the author and admins can make changes to it. | [optional]  if omitted the server will use the default value of False
**modified_at** | **datetime** | Modification date of the dashboard. | [optional] [readonly] 
**notify_list** | **[str], none_type** | List of handles of users to notify when changes are made to this dashboard. | [optional] 
**template_variable_presets** | [**[DashboardTemplateVariablePreset], none_type**](DashboardTemplateVariablePreset.md) | Array of template variables saved views. | [optional] 
**template_variables** | [**[DashboardTemplateVariables], none_type**](DashboardTemplateVariables.md) | List of template variables for this dashboard. | [optional] 
**url** | **str** | The URL of the dashboard. | [optional] [readonly] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


