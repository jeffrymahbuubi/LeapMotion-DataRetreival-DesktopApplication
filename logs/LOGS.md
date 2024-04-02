# Leap Motion Gemini Desktop Application

## To Dos

1. Wednesday - 27/03/2024 = Premilinary GUI (Graphic Using Interface) using QtDesigner

   - ![alt text](<images/image%20(1).png>)

2. Thursday - 28/03/2024 = Improve GUI

   - Fix the layout and organize the parent and children, as given,
     - `QMainWindow`
       - centralwidget
         - `QWidget - data_visualization_widget`
           - `QGroupBox - real_time_value`
           - `QGroupBox - real_time_skeleton_view`
         - `QWidget - data_management_widget`
           - `QGroupBox - data_logger`
           - `QGroupBox - device_connection`
           - `QGroupBox - saved_data_information`
           - `QLabel - logoWTMH`
           - `QPushButton - recordButton`
   - Device Connection GUI Implementation (Changing State between Disconnect to Connect)
     - Device Top Identifier: LP85571778017
     - Device Bottom Identifier: LP76907386047
     - Device Side Identifier:

3. Friday - 29/03/2024

   - Implement `recordButton` UI logic, the initial state is set to `False` when the user clicked it will turn into `True` and change the inner text into "Stop". ✅ (DONE)
   - Implement device status from "Disconnect" to "Connect" when the user connect leap motion device ✅ (DONE)
   - Show alert window when user click "Record" but there are devices that is not connected. ✅ (DONE)

4. Saturday - 30/03/2024

   - Rewrite the code to make the raw_data column to be: `timestamp` `bone_index` `thumb_start_x_device_1` `thumb_start_y_device_1` `thumb_start_z_device_1` `thumb_end_x_device_1` `thumb_end_y_device_1` `thumb_end_z_device_1` `index_start_x_device_1` `index_start_y_device_1` `index_start_z_device_1` `index_end_x_device_1` `index_end_y_device_1` `index_end_z_device_1` `middle_start_x_device_1` `middle_start_y_device_1` `middle_start_z_device_1` `middle_end_x_device_1` `middle_end_y_device_1` `middle_end_z_device_1` `ring_start_x_device_1` `ring_start_y_device_1` `ring_start_z_device_1` `ring_end_x_device_1` `ring_end_y_device_1` `ring_end_z_device_1` `pinky_start_x_device_1` `pinky_start_y_device_1` `pinky_start_z_device_1` `pinky_end_x_device_1` `pinky_end_y_device_1` `pinky_end_z_device_1`

5. Sunday - 31/03/2024
   - Let the user fill information of **Name**, **ID**, and **Date** to be used as the filename of the `.csv` file later.
   - Start the recording with condition,
     - All the leap motion devices are connected
     - User fill the **Name**, **ID**, and **Date** information
   - Connecting record button with the leapmotion logic
