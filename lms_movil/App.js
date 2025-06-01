// App.js
import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import LoginScreen from './screens/LoginScreen';
import HomeScreen from './screens/HomeScreen';
import UploadScreen from './screens/UploadScreen';
import DashboardEstudiante from './screens/DashboardEstudiante';
import SubirArchivo from './screens/SubirArchivo'; // ajusta la ruta si es diferente



const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen
          name="Login"
          component={LoginScreen}
          options={{ headerShown: false }}
        />
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{ title: 'Bienvenido' }}
        />
        <Stack.Screen 
          name="DashboardEstudiante" 
          component={DashboardEstudiante}
        />
          <Stack.Screen name="SubirArchivo" component={SubirArchivo} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
