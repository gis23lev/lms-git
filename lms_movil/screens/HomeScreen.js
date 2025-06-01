// screens/HomeScreen.js
import React from 'react';
import { View, Text, Button } from 'react-native';

export default function HomeScreen({ navigation }) {
    return (
    <View style={{ flex:1, justifyContent:'center', alignItems:'center' }}>
        <Text>¡Bienvenido a la app móvil!</Text>
        <Button title="Cerrar sesión" onPress={() => navigation.replace('Login')} />
    </View>
    );
}
